"""
Unit tests for utility functions

Author: ABDULLAH AHMAD
License: MIT
"""

import pytest
import numpy as np
import os
import tempfile
from PIL import Image

# Add src to path for testing
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import (
    load_image,
    save_image,
    create_mask_from_white_regions,
    canny_edge_detection,
    edge_guided_inpainting
)


class TestLoadImage:
    """Test image loading functionality"""

    def setup_method(self):
        """Setup test fixtures"""
        # Create a temporary test image
        self.test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        self.temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
        Image.fromarray(self.test_image).save(self.temp_file.name)
        self.temp_file.close()

    def teardown_method(self):
        """Cleanup test fixtures"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)

    def test_load_valid_image(self):
        """Test loading a valid image"""
        loaded_image = load_image(self.temp_file.name)

        assert isinstance(loaded_image, np.ndarray)
        assert len(loaded_image.shape) == 3
        assert loaded_image.shape[2] == 3  # RGB channels

    def test_load_image_with_resize(self):
        """Test loading image with resize"""
        target_size = (50, 50)
        loaded_image = load_image(self.temp_file.name, size=target_size)

        assert loaded_image.shape[:2] == target_size[::-1]  # (height, width)

    def test_load_nonexistent_image(self):
        """Test loading non-existent image raises FileNotFoundError"""
        with pytest.raises(FileNotFoundError):
            load_image('nonexistent_file.jpg')


class TestSaveImage:
    """Test image saving functionality"""

    def setup_method(self):
        """Setup test fixtures"""
        self.test_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        self.temp_dir = tempfile.mkdtemp()

    def teardown_method(self):
        """Cleanup test fixtures"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)

    def test_save_image_uint8(self):
        """Test saving uint8 image"""
        output_path = os.path.join(self.temp_dir, 'test_output.jpg')
        save_image(self.test_image, output_path)

        assert os.path.exists(output_path)

        # Load and verify
        loaded = load_image(output_path)
        assert loaded.shape == self.test_image.shape

    def test_save_image_float(self):
        """Test saving float image (should be converted to uint8)"""
        float_image = self.test_image.astype(np.float32) / 255.0
        output_path = os.path.join(self.temp_dir, 'test_float.jpg')

        save_image(float_image, output_path)
        assert os.path.exists(output_path)


class TestMaskDetection:
    """Test mask detection functionality"""

    def setup_method(self):
        """Setup test fixtures"""
        # Create image with white region
        self.test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        # Add white rectangle in center
        self.test_image[25:75, 25:75] = 255

    def test_create_mask_default_threshold(self):
        """Test mask creation with default threshold"""
        mask = create_mask_from_white_regions(self.test_image)

        assert isinstance(mask, np.ndarray)
        assert len(mask.shape) == 2  # Should be grayscale
        assert mask.dtype == np.uint8

        # Check that white region is detected
        assert np.sum(mask > 0) > 0

    def test_create_mask_custom_threshold(self):
        """Test mask creation with custom threshold"""
        # Create image with light gray instead of white
        gray_image = np.full((100, 100, 3), 200, dtype=np.uint8)

        # High threshold should not detect gray
        mask_high = create_mask_from_white_regions(gray_image, threshold=250)
        assert np.sum(mask_high > 0) == 0

        # Low threshold should detect gray
        mask_low = create_mask_from_white_regions(gray_image, threshold=150)
        assert np.sum(mask_low > 0) > 0

    def test_mask_morphological_operations(self):
        """Test that morphological operations clean up the mask"""
        # Create noisy image
        noisy_image = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)
        noisy_image[40:60, 40:60] = 255  # White square

        mask = create_mask_from_white_regions(noisy_image)

        # Mask should be cleaner than raw threshold
        assert isinstance(mask, np.ndarray)
        assert mask.dtype == np.uint8


class TestEdgeDetection:
    """Test edge detection functionality"""

    def setup_method(self):
        """Setup test fixtures"""
        # Create simple image with clear edges
        self.test_image = np.zeros((100, 100, 3), dtype=np.uint8)
        # Add white rectangle (creates edges)
        self.test_image[25:75, 25:75] = 255

    def test_canny_edge_detection_rgb(self):
        """Test Canny edge detection on RGB image"""
        edges = canny_edge_detection(self.test_image)

        assert isinstance(edges, np.ndarray)
        assert len(edges.shape) == 2  # Should be grayscale
        assert edges.dtype == np.uint8

        # Should detect some edges
        assert np.sum(edges > 0) > 0

    def test_canny_edge_detection_grayscale(self):
        """Test Canny edge detection on grayscale image"""
        gray_image = np.zeros((100, 100), dtype=np.uint8)
        gray_image[25:75, 25:75] = 255

        edges = canny_edge_detection(gray_image)

        assert isinstance(edges, np.ndarray)
        assert len(edges.shape) == 2
        assert np.sum(edges > 0) > 0

    def test_canny_parameters(self):
        """Test different Canny parameters"""
        # Sharp edges (low sigma)
        edges_sharp = canny_edge_detection(self.test_image, sigma=0.5)

        # Smooth edges (high sigma)
        edges_smooth = canny_edge_detection(self.test_image, sigma=3.0)

        # Both should detect edges but with different characteristics
        assert np.sum(edges_sharp > 0) > 0
        assert np.sum(edges_smooth > 0) > 0


class TestEdgeGuidedInpainting:
    """Test edge-guided inpainting functionality"""

    def setup_method(self):
        """Setup test fixtures"""
        # Create test image
        self.test_image = np.random.randint(100, 200, (100, 100, 3), dtype=np.uint8)

        # Create mask
        self.mask = np.zeros((100, 100), dtype=np.uint8)
        self.mask[40:60, 40:60] = 255  # Square mask in center

    def test_edge_guided_inpainting_basic(self):
        """Test basic edge-guided inpainting"""
        result, edges, edges_dilated = edge_guided_inpainting(self.test_image, self.mask)

        # Check result
        assert isinstance(result, np.ndarray)
        assert result.shape == self.test_image.shape
        assert result.dtype == np.uint8

        # Check edges
        assert isinstance(edges, np.ndarray)
        assert len(edges.shape) == 2

        # Check dilated edges
        assert isinstance(edges_dilated, np.ndarray)
        assert edges_dilated.shape == edges.shape

        # Dilated edges should have more pixels than original edges
        assert np.sum(edges_dilated > 0) >= np.sum(edges > 0)

    def test_inpainting_parameters(self):
        """Test inpainting with different parameters"""
        result1, _, _ = edge_guided_inpainting(
            self.test_image, self.mask,
            sigma=1.0, edge_weight=0.1, inpaint_radius=1
        )

        result2, _, _ = edge_guided_inpainting(
            self.test_image, self.mask,
            sigma=3.0, edge_weight=0.5, inpaint_radius=5
        )

        # Both should produce valid results
        assert result1.shape == self.test_image.shape
        assert result2.shape == self.test_image.shape

        # Results should be different
        assert not np.array_equal(result1, result2)

    def test_inpainting_preserves_unmasked_regions(self):
        """Test that inpainting preserves unmasked regions"""
        result, _, _ = edge_guided_inpainting(self.test_image, self.mask)

        # Unmasked regions should be preserved (or very similar)
        unmasked_original = self.test_image[self.mask == 0]
        unmasked_result = result[self.mask == 0]

        # Should be very similar (allowing for minor differences due to processing)
        diff = np.abs(unmasked_original.astype(float) - unmasked_result.astype(float))
        mean_diff = np.mean(diff)

        assert mean_diff < 10  # Small difference threshold


class TestIntegration:
    """Integration tests combining multiple functions"""

    def test_full_pipeline(self):
        """Test complete processing pipeline"""
        # Create test image with white mask
        image = np.random.randint(50, 200, (100, 100, 3), dtype=np.uint8)
        image[30:70, 30:70] = 255  # White square

        # Detect mask
        mask = create_mask_from_white_regions(image, threshold=240)

        # Perform inpainting
        result, edges, edges_dilated = edge_guided_inpainting(image, mask)

        # Verify complete pipeline
        assert isinstance(result, np.ndarray)
        assert result.shape == image.shape
        assert result.dtype == np.uint8

        # Mask should be detected
        assert np.sum(mask > 0) > 0

        # Edges should be detected
        assert np.sum(edges > 0) > 0


if __name__ == '__main__':
    pytest.main([__file__])
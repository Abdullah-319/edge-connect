"""
Main FaceReconstructor class for EdgeConnect Face Reconstruction

Author: ABDULLAH AHMAD
License: MIT
"""

import os
import numpy as np
import cv2
from PIL import Image
from typing import Tuple, Optional, Dict, Any
import matplotlib.pyplot as plt

from .utils import (
    load_image,
    save_image,
    create_mask_from_white_regions,
    edge_guided_inpainting
)


class FaceReconstructor:
    """
    Main class for EdgeConnect-inspired face reconstruction
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the FaceReconstructor

        Args:
            config: Configuration dictionary with parameters
        """
        self.config = config or self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration"""
        return {
            'threshold': 240,
            'edge_sigma': 2,
            'edge_weight': 0.3,
            'inpaint_radius': 3,
            'target_size': None,
            'save_intermediate': True,
            'output_format': 'jpg',
            'output_quality': 95
        }

    def process_image(self, image_path: str, output_dir: str = './output',
                     mask_threshold: Optional[int] = None,
                     target_size: Optional[Tuple[int, int]] = None) -> Dict[str, np.ndarray]:
        """
        Process a single image with face reconstruction

        Args:
            image_path: Path to input image
            output_dir: Output directory
            mask_threshold: Override mask detection threshold
            target_size: Target size for processing (width, height)

        Returns:
            Dictionary containing results
        """
        # Load image
        size = target_size or self.config.get('target_size')
        image = load_image(image_path, size=size)

        # Get threshold
        threshold = mask_threshold or self.config['threshold']

        # Create mask from white regions
        mask = create_mask_from_white_regions(image, threshold=threshold)

        # Check if mask was detected
        if np.sum(mask) == 0:
            raise ValueError(f"No white regions detected with threshold {threshold}")

        # Perform edge-guided inpainting
        result, edges, edges_dilated = edge_guided_inpainting(
            image, mask,
            sigma=self.config['edge_sigma'],
            edge_weight=self.config['edge_weight'],
            inpaint_radius=self.config['inpaint_radius']
        )

        # Save results if requested
        if self.config['save_intermediate']:
            self._save_results(image_path, image, mask, edges, result, output_dir)

        return {
            'original': image,
            'mask': mask,
            'edges': edges,
            'edges_dilated': edges_dilated,
            'result': result
        }

    def _save_results(self, image_path: str, image: np.ndarray, mask: np.ndarray,
                     edges: np.ndarray, result: np.ndarray, output_dir: str) -> None:
        """Save all results to files"""
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Generate base filename
        base_name = os.path.splitext(os.path.basename(image_path))[0]

        # Save individual results
        save_image(result, os.path.join(output_dir, f"{base_name}_reconstructed.jpg"),
                  quality=self.config['output_quality'])
        save_image(mask, os.path.join(output_dir, f"{base_name}_mask.jpg"))
        save_image(edges, os.path.join(output_dir, f"{base_name}_edges.jpg"))

        # Create and save comparison
        comparison = np.hstack([image, result])
        save_image(comparison, os.path.join(output_dir, f"{base_name}_comparison.jpg"))

    def visualize_results(self, results: Dict[str, np.ndarray],
                         figsize: Tuple[int, int] = (15, 10)) -> None:
        """
        Visualize reconstruction results

        Args:
            results: Results dictionary from process_image
            figsize: Figure size for matplotlib
        """
        fig, axes = plt.subplots(2, 3, figsize=figsize)

        # Original image
        axes[0, 0].imshow(results['original'])
        axes[0, 0].set_title('Original Image with Mask')
        axes[0, 0].axis('off')

        # Detected mask
        axes[0, 1].imshow(results['mask'], cmap='gray')
        axes[0, 1].set_title('Detected Mask')
        axes[0, 1].axis('off')

        # Edges
        axes[0, 2].imshow(results['edges'], cmap='gray')
        axes[0, 2].set_title('Canny Edges')
        axes[0, 2].axis('off')

        # Dilated edges
        axes[1, 0].imshow(results['edges_dilated'], cmap='gray')
        axes[1, 0].set_title('Dilated Edges')
        axes[1, 0].axis('off')

        # Result
        axes[1, 1].imshow(results['result'])
        axes[1, 1].set_title('Reconstructed Result')
        axes[1, 1].axis('off')

        # Comparison
        comparison = np.hstack([results['original'], results['result']])
        axes[1, 2].imshow(comparison)
        axes[1, 2].set_title('Before vs After')
        axes[1, 2].axis('off')

        plt.tight_layout()
        plt.show()

    def batch_process(self, input_dir: str, output_dir: str,
                     file_extensions: Tuple[str, ...] = ('.jpg', '.jpeg', '.png', '.bmp')) -> None:
        """
        Process multiple images in a directory

        Args:
            input_dir: Input directory containing images
            output_dir: Output directory for results
            file_extensions: Supported file extensions
        """
        if not os.path.exists(input_dir):
            raise FileNotFoundError(f"Input directory not found: {input_dir}")

        # Find all image files
        image_files = []
        for file in os.listdir(input_dir):
            if file.lower().endswith(file_extensions):
                image_files.append(os.path.join(input_dir, file))

        if not image_files:
            print(f"No image files found in {input_dir}")
            return

        print(f"Found {len(image_files)} images to process...")

        # Process each image
        for i, image_path in enumerate(image_files, 1):
            try:
                print(f"Processing {i}/{len(image_files)}: {os.path.basename(image_path)}")
                self.process_image(image_path, output_dir)
                print(f"✓ Completed: {os.path.basename(image_path)}")
            except Exception as e:
                print(f"✗ Error processing {os.path.basename(image_path)}: {e}")

        print(f"Batch processing completed. Results saved to {output_dir}")

    def update_config(self, **kwargs) -> None:
        """Update configuration parameters"""
        self.config.update(kwargs)

    def get_config(self) -> Dict[str, Any]:
        """Get current configuration"""
        return self.config.copy()

    def create_sample_image(self, size: int = 256, output_path: str = 'sample_face.jpg') -> str:
        """
        Create a sample face image with white mask for testing

        Args:
            size: Image size
            output_path: Output path for sample image

        Returns:
            Path to created sample image
        """
        # Create a simple face-like image
        image = np.ones((size, size, 3), dtype=np.uint8) * 200

        center_x, center_y = size // 2, size // 2

        # Face outline
        cv2.ellipse(image, (center_x, center_y), (80, 100), 0, 0, 360, (180, 150, 120), -1)

        # Eyes
        cv2.circle(image, (center_x - 25, center_y - 20), 8, (50, 50, 50), -1)
        cv2.circle(image, (center_x + 25, center_y - 20), 8, (50, 50, 50), -1)

        # Mouth
        cv2.ellipse(image, (center_x, center_y + 30), (15, 8), 0, 0, 180, (100, 50, 50), 2)

        # Add white nose mask
        nose_points = np.array([
            [center_x - 10, center_y - 5],
            [center_x + 10, center_y - 5],
            [center_x + 8, center_y + 15],
            [center_x - 8, center_y + 15]
        ], np.int32)

        cv2.fillPoly(image, [nose_points], (255, 255, 255))

        # Save sample image
        save_image(image, output_path)
        print(f"Sample image created: {output_path}")

        return output_path
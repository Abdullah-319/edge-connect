#!/usr/bin/env python3
"""
Test script for face reconstruction using EdgeConnect
"""

import os
import sys
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def create_mask_from_white_regions(image, threshold=240):
    """Create mask from white regions in the image (like the nose mask)"""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # Create mask where white regions are
    mask = (gray > threshold).astype(np.uint8) * 255

    # Apply morphological operations to clean up the mask
    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask

def canny_edge_detection(image, sigma=2, low_threshold=0.1, high_threshold=0.2):
    """Apply Canny edge detection"""
    # Convert to grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (0, 0), sigma)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, int(low_threshold * 255), int(high_threshold * 255))

    return edges

def edge_guided_inpainting(image, mask, sigma=2):
    """Perform edge-guided inpainting using traditional methods"""
    # Step 1: Extract edges from the non-masked regions
    edges = canny_edge_detection(image, sigma=sigma)

    # Step 2: Mask the edges (remove edges in masked regions)
    edges_masked = edges.copy()
    edges_masked[mask > 0] = 0

    # Step 3: Extend edges into masked regions using morphological operations
    kernel = np.ones((3,3), np.uint8)
    edges_dilated = cv2.dilate(edges_masked, kernel, iterations=2)

    # Step 4: Perform inpainting using Telea method
    inpainted = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

    # Step 5: Enhance inpainting using Fast Marching method
    inpainted_fm = cv2.inpaint(image, mask, 3, cv2.INPAINT_NS)

    # Step 6: Blend results based on edge guidance
    edge_weight = 0.3
    final_result = (1 - edge_weight) * inpainted + edge_weight * inpainted_fm

    return final_result.astype(np.uint8), edges, edges_dilated

def create_sample_face_with_mask():
    """Create a sample face image with a white nose mask for testing"""
    # Create a simple face-like image
    size = 256
    image = np.ones((size, size, 3), dtype=np.uint8) * 200  # Light background

    # Add some facial features
    center_x, center_y = size // 2, size // 2

    # Face outline (ellipse)
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

    return image

def test_reconstruction():
    """Test the face reconstruction pipeline"""
    print("Creating sample face with mask...")

    # Create sample image
    sample_image = create_sample_face_with_mask()

    # Save sample image
    os.makedirs('./input_images', exist_ok=True)
    sample_path = './input_images/sample_face_with_mask.jpg'
    Image.fromarray(sample_image).save(sample_path)
    print(f"Sample image saved to {sample_path}")

    # Load the image
    image = np.array(Image.open(sample_path).convert('RGB'))

    # Resize to standard size
    image = cv2.resize(image, (256, 256))

    # Create mask from white regions
    mask = create_mask_from_white_regions(image)

    # Perform edge-guided inpainting
    result, edges, edges_dilated = edge_guided_inpainting(image, mask)

    # Save results
    os.makedirs('./output', exist_ok=True)
    Image.fromarray(result).save('./output/reconstructed.jpg')
    Image.fromarray(mask).save('./output/mask.jpg')
    Image.fromarray(edges).save('./output/edges.jpg')

    print("Results saved to ./output/")
    print("- reconstructed.jpg: Final result")
    print("- mask.jpg: Detected mask")
    print("- edges.jpg: Edge detection")

    # Create comparison image
    comparison = np.hstack([image, result])
    Image.fromarray(comparison).save('./output/comparison.jpg')
    print("- comparison.jpg: Before vs After")

    print("\nReconstruction completed successfully!")
    return result, mask, edges

if __name__ == "__main__":
    test_reconstruction()
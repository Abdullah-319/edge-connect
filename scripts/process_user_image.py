#!/usr/bin/env python3
"""
Process user's image with EdgeConnect-style face reconstruction
"""

import os
import sys
import argparse
import numpy as np
import cv2
from PIL import Image

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

def process_image(image_path, output_dir="./output", mask_threshold=240, target_size=None):
    """Process a single image with face reconstruction"""

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    # Load the image
    image = np.array(Image.open(image_path).convert('RGB'))
    original_size = image.shape[:2]

    # Resize if target size is specified
    if target_size:
        image = cv2.resize(image, target_size)

    print(f"Processing image: {image_path}")
    print(f"Image size: {image.shape}")

    # Create mask from white regions
    mask = create_mask_from_white_regions(image, threshold=mask_threshold)

    # Check if mask was detected
    if np.sum(mask) == 0:
        print(f"Warning: No white regions detected with threshold {mask_threshold}")
        print("Try adjusting the threshold or check if your image has white masks")
        return None

    print(f"Mask detected: {np.sum(mask > 0)} pixels")

    # Perform edge-guided inpainting
    result, edges, edges_dilated = edge_guided_inpainting(image, mask)

    # Create output directory
    os.makedirs(output_dir, exist_ok=True)

    # Generate output filename
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    # Save results
    Image.fromarray(result).save(os.path.join(output_dir, f"{base_name}_reconstructed.jpg"))
    Image.fromarray(mask).save(os.path.join(output_dir, f"{base_name}_mask.jpg"))
    Image.fromarray(edges).save(os.path.join(output_dir, f"{base_name}_edges.jpg"))

    # Create comparison image
    comparison = np.hstack([image, result])
    Image.fromarray(comparison).save(os.path.join(output_dir, f"{base_name}_comparison.jpg"))

    print(f"Results saved to {output_dir}/")
    print(f"- {base_name}_reconstructed.jpg: Final result")
    print(f"- {base_name}_mask.jpg: Detected mask")
    print(f"- {base_name}_edges.jpg: Edge detection")
    print(f"- {base_name}_comparison.jpg: Before vs After")

    return result, mask, edges

def main():
    parser = argparse.ArgumentParser(description='Face reconstruction using EdgeConnect-style inpainting')
    parser.add_argument('image_path', help='Path to input image')
    parser.add_argument('--output', '-o', default='./output', help='Output directory')
    parser.add_argument('--threshold', '-t', type=int, default=240, help='White mask detection threshold (0-255)')
    parser.add_argument('--size', '-s', type=int, nargs=2, metavar=('WIDTH', 'HEIGHT'), help='Target size for processing')

    args = parser.parse_args()

    try:
        target_size = tuple(args.size) if args.size else None
        result = process_image(args.image_path, args.output, args.threshold, target_size)

        if result is not None:
            print("\nFace reconstruction completed successfully!")
        else:
            print("\nFace reconstruction failed. Please check the input image and parameters.")

    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())
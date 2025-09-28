"""
Utility functions for EdgeConnect Face Reconstruction

Author: ABDULLAH AHMAD
License: MIT
"""

import os
import numpy as np
import cv2
from PIL import Image
from typing import Tuple, Optional, Union


def load_image(image_path: str, size: Optional[Tuple[int, int]] = None) -> np.ndarray:
    """Load and preprocess image"""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = Image.open(image_path).convert('RGB')
    if size:
        image = image.resize(size, Image.LANCZOS)
    return np.array(image)


def save_image(image: np.ndarray, output_path: str, quality: int = 95) -> None:
    """Save image array to file"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    if image.dtype != np.uint8:
        image = (image * 255).astype(np.uint8)

    pil_image = Image.fromarray(image)
    pil_image.save(output_path, quality=quality, optimize=True)


def create_mask_from_white_regions(image: np.ndarray, threshold: int = 240) -> np.ndarray:
    """Create mask from white regions in the image"""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    mask = (gray > threshold).astype(np.uint8) * 255

    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    return mask


def canny_edge_detection(image: np.ndarray, sigma: float = 2,
                        low_threshold: float = 0.1, high_threshold: float = 0.2) -> np.ndarray:
    """Apply Canny edge detection"""
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image

    blurred = cv2.GaussianBlur(gray, (0, 0), sigma)
    edges = cv2.Canny(blurred, int(low_threshold * 255), int(high_threshold * 255))

    return edges


def edge_guided_inpainting(image: np.ndarray, mask: np.ndarray, sigma: float = 2,
                          edge_weight: float = 0.3, inpaint_radius: int = 3) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Perform edge-guided inpainting using traditional methods"""
    edges = canny_edge_detection(image, sigma=sigma)
    edges_masked = edges.copy()
    edges_masked[mask > 0] = 0

    kernel = np.ones((3, 3), np.uint8)
    edges_dilated = cv2.dilate(edges_masked, kernel, iterations=2)

    inpainted = cv2.inpaint(image, mask, inpaint_radius, cv2.INPAINT_TELEA)
    inpainted_fm = cv2.inpaint(image, mask, inpaint_radius, cv2.INPAINT_NS)

    final_result = (1 - edge_weight) * inpainted + edge_weight * inpainted_fm
    return final_result.astype(np.uint8), edges, edges_dilated
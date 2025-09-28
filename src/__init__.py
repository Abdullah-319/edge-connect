"""
EdgeConnect Face Reconstruction Package

A robust implementation of EdgeConnect-inspired face reconstruction
for inpainting masked facial regions.

Author: ABDULLAH AHMAD
License: MIT
"""

__version__ = "1.0.0"
__author__ = "ABDULLAH AHMAD"
__email__ = "your.email@example.com"

from .face_reconstructor import FaceReconstructor
from .utils import (
    create_mask_from_white_regions,
    canny_edge_detection,
    edge_guided_inpainting,
    load_image,
    save_image
)

__all__ = [
    "FaceReconstructor",
    "create_mask_from_white_regions",
    "canny_edge_detection",
    "edge_guided_inpainting",
    "load_image",
    "save_image"
]
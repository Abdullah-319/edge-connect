#!/usr/bin/env python3
"""
Batch processing script for EdgeConnect Face Reconstruction

Author: ABDULLAH AHMAD
License: MIT
"""

import os
import sys
import argparse
from typing import List, Tuple

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from face_reconstructor import FaceReconstructor


def main():
    parser = argparse.ArgumentParser(
        description='Batch process multiple images for face reconstruction'
    )
    parser.add_argument(
        'input_dir',
        help='Input directory containing images'
    )
    parser.add_argument(
        'output_dir',
        help='Output directory for results'
    )
    parser.add_argument(
        '--threshold', '-t',
        type=int,
        default=240,
        help='White mask detection threshold (0-255)'
    )
    parser.add_argument(
        '--size', '-s',
        type=int,
        nargs=2,
        metavar=('WIDTH', 'HEIGHT'),
        help='Target size for processing'
    )
    parser.add_argument(
        '--extensions', '-e',
        nargs='+',
        default=['.jpg', '.jpeg', '.png', '.bmp'],
        help='File extensions to process'
    )

    args = parser.parse_args()

    # Configure reconstructor
    config = {
        'threshold': args.threshold,
        'target_size': tuple(args.size) if args.size else None,
        'save_intermediate': True
    }

    reconstructor = FaceReconstructor(config)

    try:
        # Process batch
        reconstructor.batch_process(
            args.input_dir,
            args.output_dir,
            file_extensions=tuple(args.extensions)
        )
        print("✅ Batch processing completed successfully!")
        return 0

    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
"""Image preprocessing script.

Loads images from the input directory, converts them to grayscale, applies
Gaussian blur and Otsu's thresholding, then saves the binary images to the
output directory.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import cv2
import numpy as np


def preprocess_images(
    input_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    verbose: bool = False,
) -> None:
    """Preprocess images found in *input_dir* and save results to *output_dir*."""
    base_dir = Path(__file__).resolve().parents[1]
    if input_dir is None:
        input_dir = base_dir / "input"
    if output_dir is None:
        output_dir = base_dir / "output" / "preprocessed"

    output_dir.mkdir(parents=True, exist_ok=True)

    patterns = ("*.png", "*.jpg", "*.jpeg")
    files = []
    for pattern in patterns:
        files.extend(sorted(input_dir.glob(pattern)))

    for img_path in files:
        img = cv2.imread(str(img_path))
        if img is None:
            if verbose:
                print(f"Warning: Unable to read {img_path}")
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        out_path = output_dir / img_path.name
        cv2.imwrite(str(out_path), thresh)
        if verbose:
            print(f"Processed {img_path} -> {out_path}")
        else:
            print(f"Processed {img_path.name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Preprocess images with Gaussian blur and Otsu's thresholding"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()
    preprocess_images(verbose=args.verbose)

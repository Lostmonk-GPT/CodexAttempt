"""Tesseract OCR wrapper."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

import cv2
import pytesseract


def ocr_tesseract(
    input_dir: Optional[Path] = None,
    output_dir: Optional[Path] = None,
    lang: str = "eng",
) -> None:
    """Run OCR on images in *input_dir* and save text files to *output_dir*."""
    base_dir = Path(__file__).resolve().parents[1]
    if input_dir is None:
        input_dir = base_dir / "output" / "preprocessed"
    if output_dir is None:
        output_dir = base_dir / "output" / "ocr_results"

    output_dir.mkdir(parents=True, exist_ok=True)

    patterns = ("*.png", "*.jpg", "*.jpeg")
    files = []
    for pattern in patterns:
        files.extend(sorted(input_dir.glob(pattern)))

    for img_path in files:
        img = cv2.imread(str(img_path))
        if img is None:
            print(f"Warning: Unable to read {img_path}")
            continue
        text = pytesseract.image_to_string(img, lang=lang)
        out_path = output_dir / f"{img_path.stem}.txt"
        out_path.write_text(text, encoding="utf-8")
        print(f"{img_path.name}: {len(text)} chars")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Tesseract OCR on images")
    parser.add_argument(
        "--lang",
        default="eng",
        help="Tesseract language code (default: eng)",
    )
    args = parser.parse_args()
    ocr_tesseract(lang=args.lang)

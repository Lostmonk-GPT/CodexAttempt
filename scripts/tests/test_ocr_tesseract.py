import cv2
import numpy as np
from pathlib import Path
from scripts.ocr_tesseract import ocr_tesseract


def test_ocr_tesseract(tmp_path):
    input_dir = tmp_path / "preprocessed"
    output_dir = tmp_path / "ocr_results"
    input_dir.mkdir()
    output_dir.mkdir()

    img = np.full((40, 100, 3), 255, dtype=np.uint8)
    cv2.putText(
        img, "hi", (5, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA
    )
    cv2.imwrite(str(input_dir / "sample.png"), img)

    ocr_tesseract(input_dir=input_dir, output_dir=output_dir, lang="eng")

    out_file = output_dir / "sample.txt"
    assert out_file.exists()
    text = out_file.read_text(encoding="utf-8").strip()
    assert len(text) > 0

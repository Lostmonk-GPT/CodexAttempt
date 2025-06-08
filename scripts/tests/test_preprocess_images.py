import cv2
import numpy as np
from pathlib import Path
from scripts.preprocess_images import preprocess_images


def test_preprocess_images(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()

    img1 = np.zeros((10, 10, 3), dtype=np.uint8)
    img1[5:, :] = 255
    cv2.imwrite(str(input_dir / "test1.jpg"), img1)

    img2 = np.full((8, 8, 3), 128, dtype=np.uint8)
    cv2.imwrite(str(input_dir / "test2.png"), img2)

    preprocess_images(input_dir=input_dir, output_dir=output_dir, verbose=True)

    out1 = output_dir / "test1.jpg"
    out2 = output_dir / "test2.png"
    assert out1.exists()
    assert out2.exists()

    data = cv2.imread(str(out1), cv2.IMREAD_GRAYSCALE)
    unique_vals = set(np.unique(data))
    assert 0 in unique_vals and 255 in unique_vals
    assert len(unique_vals) <= 3

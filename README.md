# 🧠 OCR Pipeline – Modular Codex System

This repository is for building, testing, and evaluating OCR (Optical Character Recognition) components using modular Python scripts. Each step is implemented and tested independently for easy debugging and integration.

---

## 📁 Folder Structure

```bash
/input/                 # Raw scanned images
/output/
  /preprocessed/        # Preprocessed images
  /ocr_results/         # OCR outputs
  /logs/                # Evaluation logs
/ground_truth/          # Clean reference answers
/scripts/               # All modular Python files
/scripts/tests/         # Pytest unit tests

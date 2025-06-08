# 🤖 AGENTS.md – Codex Contribution Guide

This document provides instructions for Codex (or other AI agents) when generating code or making contributions to this repository.

---

## 🧱 Project Principles

- **Modularity First**: Each script should do one thing well and live in `/scripts/`
- **Debuggability**: Keep logic clear, minimize hidden state or tight coupling
- **Automation-Friendly**: Scripts should run from CLI, support batch input, and use standard libraries

---

## 📂 Directory Conventions

- **Input/Output Folders**:
  - Read from `/input/`, write to `/output/`
  - Ground truth data lives in `/ground_truth/`

- **Scripts Folder**:
  - Place all code modules in `/scripts/`
  - Name files clearly (e.g. `ocr_tesseract.py`, `evaluate_results.py`)
  - Place test files in `/scripts/tests/`, named `test_<module>.py`

---

## 🔬 Testing Rules

- Use `pytest` for all tests
- Cover main logic paths in each module
- Include test data in `/input/` or generate it inline
- Do not access the internet; assume offline sandbox

---

## 🧪 Module Checklist (for Codex)

When creating a new script:
- [ ] Save it in `/scripts/`
- [ ] Use CLI args if the script accepts input
- [ ] Log to stdout or `/output/logs/`
- [ ] Validate file paths before access
- [ ] Include a basic docstring and comments
- [ ] Add a matching unit test in `/scripts/tests/`
- [ ] Follow PEP8 and format with `black`

---

## 📎 Codex Style Rules

- No external services or APIs unless specified
- Prefer OpenCV, NumPy, standard Python libs
- No GUI or web dependencies
- Use `if __name__ == "__main__"` when applicable

---

## 🧾 Logging + Prompts

- Log all prompt completions in `Codex_Prompt_Archive.md`
- Use `Bug_Log.md` to document errors or odd Codex behavior

---

## ✅ Output Validation

- OCR outputs go in `/output/ocr_results/`
- Evaluation outputs go in `/output/logs/`
- Clean input for comparison goes in `/ground_truth/`


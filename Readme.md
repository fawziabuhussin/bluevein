# Bluevine Check‑Approval Strategy

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Build](https://img.shields.io/badge/Status-Prototype-orange)

> **NOTE  ❗**  The original data file *Bluevine\_Analyst\_Exam\_-\_Data.xlsx* is **confidential** and **MUST NOT** be committed to this repository. Follow the instructions below to obtain it securely before running the code.

---

## Table of Contents

1. [Overview](#overview)
2. [Repository layout](#repository-layout)
3. [Prerequisites](#prerequisites)
4. [Getting the data (confidential)](#getting-the-data-confidential)
5. [Quick‑start: generate figures & decisions](#quick-start)
6. [Producing the PDF report](#building-the-report)
7. [FAQ](#faq)
8. [License](#license)

---

<a id="overview"></a>

## 1 · Overview

This repo contains:

* A **rule‑based decision engine** (`data_analyst_exam.py`) that tags each check with `Post / Hold6d / Reject` based on fraud‑score, dollar amount and customer history.
* A lightweight **EDA notebook / script** that creates a full set of plots used in the accompanying PDF report (see `figures/` once generated).
* A **LaTeX report** (`main.tex`) that stitches the business answers with the generated plots.

<a id="repository-layout"></a>

## 2 · Repository layout

```
.
├── README.md               <- *you are here*
├── requirements.txt        <- pip dependencies
├── data_analyst_exam.py    <- main analysis / decision engine
├── main.tex                <- LaTeX report
├── figures/                <- auto‑generated PNGs (ignored by Git)
└── data/                   <- **git‑ignored** confidential Excel file
```

<a id="prerequisites"></a>

## 3 · Prerequisites

| Tool   | Version         | Notes                                 |
| ------ | --------------- | ------------------------------------- |
| Python |  ≥ 3.10         | Use `pyenv` / `conda` / system Python |
| LaTeX  | TeX Live 2023 + | Only needed to compile the report     |
| Git    | any             |                                       |

Install the Python packages:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

<a id="getting-the-data-confidential"></a>

## 4 · Getting the data (confidential)

1. Log in to the **Bluevine Analyst Portal**
   [https://portal.bluevine.com/analyst‑exam](https://portal.bluevine.com/analyst‑exam) *(internal access required)*.
2. Download the file **`Bluevine_Analyst_Exam_-_Data.xlsx`**.
3. Move the file to the repo under `data/`:

   ```bash
   mkdir -p data
   mv /path/to/Bluevine_Analyst_Exam_-_Data.xlsx data/
   ```

> The `.gitignore` already excludes `data/*` to prevent accidental commits.

<a id="quick-start"></a>

## 5 · Quick‑start: generate figures & decisions

```bash
python data_analyst_exam.py
```

The script will:

* Read `data/Bluevine_Analyst_Exam_-_Data.xlsx`.
* Output `figures/Figure_*.png` (EDA plots).
* Create `bluevine_with_decision.csv` containing the new `decision` column.
* Print a KPI table to the console.

You can tweak thresholds in the `decide()` function.

<a id="building-the-report"></a>

## 6 · Producing the PDF report

Two options:

### A — Overleaf (no local TeX needed)

1. Create a private Overleaf project.
2. Upload `main.tex` and all PNGs inside `figures/`.
3. Hit *Recompile* — the badge in Question 3 links to the Appendix automatically.

### B — Local TeX Live

```bash
pdflatex main.tex   # run twice for references
```

The PDF (`main.pdf`) will appear in the same directory.

<a id="faq"></a>

## 7 · FAQ

| Q                                                  | A                                                                                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| *I changed the rules, how do I update the report?* | Re‑run `python data_analyst_exam.py` to regenerate `figures/`, then re‑compile `main.tex`. |
| *I get `ModuleNotFoundError`*                      | Ensure the venv is activated and you installed `requirements.txt`.                         |
| *Plots don’t show in Overleaf*                     | Confirm the PNGs are uploaded and names match (`Figure_1.png`, etc.).                      |

<a id="license"></a>

## 8 · License

Copyright © 2025 Bluevine.  Internal analyst exercise.
Distribution or disclosure of the raw data file is prohibited.

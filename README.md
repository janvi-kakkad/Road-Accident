# Road Accident Analysis (India)

![Project](https://img.shields.io/badge/Domain-Road%20Safety-darkgreen) ![Python](https://img.shields.io/badge/Python-Data%20Pipeline-blue) ![KNIME](https://img.shields.io/badge/KNIME-Workflow-orange) ![Tableau](https://img.shields.io/badge/Tableau-Dashboards-purple)

A complete end-to-end analytics project combining Python, KNIME, and Tableau to understand accident severity trends and actionable safety insights.

---

## Why this project matters

Road safety analysis helps identify high-risk patterns across driver behavior, environmental conditions, and location context. This repository is organized so both technical and non-technical readers can understand the full workflow.

---

## Repository structure

- data/raw: original dataset
- data/processed: generated clean and summary outputs
- output: final visual outputs (Tableau previews + KNIME workflow visual)
- src: modular Python pipeline
- notebooks: exploration notebook
- tableau: Tableau source workbook
- knime: KNIME source workflow package
- docs: step-by-step explanations

---

## Quick start

1. Install dependencies
- pip install -r requirements.txt

2. Run the Python pipeline
- python src/run_pipeline.py

3. Open visual workflows
- Tableau workbook: tableau/DAV innovative.twbx
- KNIME workflow package: knime/KNIME_project3.knwf
- Ready previews: output/tableau and output/knime

---

## Workflow at a glance

### Python

- Load and clean raw accident data
- Normalize missing values and engineer time features
- Build analysis-ready table with severity score
- Export curated tables for BI/reporting

See: docs/04_python_pipeline.md

### KNIME

- Ingestion -> cleaning -> EDA -> correlation -> ML (RF + DT)
- Performance measured via scorer nodes

See: docs/02_knime_workflow.md

### Tableau

- 11 worksheet design
- 5 stakeholder-focused dashboards

See: docs/03_tableau_assets.md

---

## Tableau image gallery

### Dashboards (5)

| Dashboard | Preview |
|---|---|
| Driver Risk Profile & Campaign Planning (RSA Focus) | ![Driver Risk](output/tableau/dashboards/Driver%20Risk%20Profile%20%26%20Campaign%20Planning%20%28RSA%20Focus%29.png) |
| Final Project Summary & Theoretical Findings | ![Final Summary](output/tableau/dashboards/Final%20Project%20Summary%20%26%20Theoretical%20Findings.png) |
| Infrastructure & Environmental Review (RSA/Municipality) | ![Infrastructure Review](output/tableau/dashboards/Infrastructure%20%26%20Environmental%20Review%20%28RSAMunicipality%29.png) |
| Insurance and Liability Risk (Actuary Focus) | ![Insurance Risk](output/tableau/dashboards/Insurance%20and%20Liability%20Risk%20%28Actuary%20Focus%29.png) |
| Traffic Operations & Enforcement (Police Focus) | ![Traffic Ops](output/tableau/dashboards/Traffic%20Operations%20%26%20Enforcement%20%28Police%20Focus%29.png) |

### Worksheets (available previews)

| Worksheet | Preview |
|---|---|
| 1 - Police Light-Day Risk Map | ![WS1](output/tableau/worksheets/1%20-%20Police%20Light-Day%20Risk%20Map.png) |
| 2 - RSA Age Risk Rate | ![WS2](output/tableau/worksheets/2%20-%20RSA%20Age%20Risk%20Rate.png) |
| 3 - RSA Experience Risk Rate | ![WS3](output/tableau/worksheets/3%20-%20RSA%20Experience%20Risk%20Rate.png) |
| 4 - Driver Sex Distribution | ![WS4](output/tableau/worksheets/4%20-%20Driver%20Sex%20Distribution.png) |
| 5 - Overall Severity Proportion Pie | ![WS5](output/tableau/worksheets/5%20-%20Overall%20Severity%20Proportion%20Pie.png) |
| 6 - Police High-Risk Areas | ![WS6](output/tableau/worksheets/6%20-%20Police%20High-Risk%20Areas.png) |
| 7 - Insurance Vehicle Volume (Bubbles) | ![WS7](output/tableau/worksheets/7%20-%20Insurance%20Vehicle%20Volume%20%28Bubbles%29.png) |
| 8 - Accident Scale Scatter | ![WS8](output/tableau/worksheets/8%20-%20Accident%20Scale%20Scatter.png) |
| 9 - RSA Road & Junction Risk (Highlight) | ![WS9](output/tableau/worksheets/9%20-%20RSA%20Road%20%26%20Junction%20Risk%20%28Highlight%29.png) |
| 10 - Top Causes Lollipop Chart | ![WS10](output/tableau/worksheets/10%20-%20Top%20Causes%20Lollipop%20Chart.png) |
| 11 - RSA Weather Risk (Dot Plot) | ![WS11](output/tableau/worksheets/11%20-%20RSA%20Weather%20Risk%20%28Dot%20Plot%29.png) |

---

## KNIME workflow visual

![KNIME Workflow](output/knime/KNIME_workflow.svg)

---

## Professional notes

- The repository intentionally avoids storing redundant temporary extraction folders and duplicate archives.
- All included assets are either source files or meaningful project artifacts.
- Missing worksheet previews are explicitly documented instead of fabricated.

---


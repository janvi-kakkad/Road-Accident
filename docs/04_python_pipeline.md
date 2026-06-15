# Python Pipeline

Main runner: src/run_pipeline.py

## Module Structure

- src/preprocessing.py
  - load_data
  - normalize_missing_values
  - add_time_features
  - convert_numeric_columns
  - make_analysis_ready

- src/analysis.py
  - severity_distribution
  - severity_by_day
  - severity_by_hour
  - severity_by_area
  - hotspot_area_junction
  - cause_severity

- src/exporters.py
  - export_table
  - export_all_tables

## Outputs

Generated files are written to data/processed:

- road_cleaned_for_knime_tableau.csv
- severity_distribution.csv
- severity_by_day.csv
- severity_by_hour.csv
- severity_by_area.csv
- hotspot_area_junction.csv
- cause_severity.csv

## Run

From project root:

python src/run_pipeline.py

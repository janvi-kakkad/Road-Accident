from __future__ import annotations

from pathlib import Path

from analysis import (
    cause_severity,
    hotspot_area_junction,
    severity_by_area,
    severity_by_day,
    severity_by_hour,
    severity_distribution,
)
from exporters import export_all_tables
from preprocessing import (
    add_time_features,
    convert_numeric_columns,
    load_data,
    make_analysis_ready,
    normalize_missing_values,
)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    raw_data_path = project_root / "data" / "raw" / "Road.csv"
    out_dir = project_root / "data" / "processed"

    raw_df = load_data(str(raw_data_path))
    cleaned_df = normalize_missing_values(raw_df)
    time_df = add_time_features(cleaned_df)
    numeric_df = convert_numeric_columns(time_df)
    analysis_df = make_analysis_ready(numeric_df)

    tables = {
        "road_cleaned_for_knime_tableau": analysis_df,
        "severity_distribution": severity_distribution(analysis_df),
        "severity_by_day": severity_by_day(analysis_df),
        "severity_by_hour": severity_by_hour(analysis_df),
        "severity_by_area": severity_by_area(analysis_df),
        "hotspot_area_junction": hotspot_area_junction(analysis_df),
        "cause_severity": cause_severity(analysis_df),
    }

    export_all_tables(tables, out_dir)
    print("Pipeline complete. Processed files are in data/processed/.")


if __name__ == "__main__":
    main()

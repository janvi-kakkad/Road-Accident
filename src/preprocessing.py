from __future__ import annotations

import numpy as np
import pandas as pd


MISSING_TOKENS = {"", "na", "n/a", "null", "none"}


def load_data(path: str) -> pd.DataFrame:
    """Load CSV with a safe fallback encoding."""
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")


def normalize_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize common text placeholders to NaN."""
    out = df.copy()

    def normalize_cell(value: object) -> object:
        if isinstance(value, str):
            token = value.strip()
            if token.lower() in MISSING_TOKENS:
                return np.nan
            return token
        return value

    return out.applymap(normalize_cell)


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    """Parse time and engineer hour/time-band features."""
    out = df.copy()

    if "Time" in out.columns:
        out["Time_parsed"] = pd.to_datetime(out["Time"], errors="coerce", dayfirst=True)
        out["hour_from_time"] = out["Time_parsed"].dt.hour
    else:
        out["Time_parsed"] = pd.NaT
        out["hour_from_time"] = np.nan

    if "Hour of Day" in out.columns:
        out["Hour of Day"] = pd.to_numeric(out["Hour of Day"], errors="coerce")
        out["hour_final"] = out["Hour of Day"].fillna(out["hour_from_time"])
    else:
        out["hour_final"] = out["hour_from_time"]

    def hour_band(hour: float) -> str:
        if pd.isna(hour):
            return "Unknown"
        hour = int(hour)
        if 5 <= hour < 12:
            return "Morning"
        if 12 <= hour < 17:
            return "Afternoon"
        if 17 <= hour < 21:
            return "Evening"
        return "Night"

    out["time_band"] = out["hour_final"].apply(hour_band)
    return out


def convert_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert known numeric columns if present."""
    out = df.copy()
    numeric_cols = [
        "High Severity Count",
        "High Severity Rate",
        "Hour of Day",
        "Number of casualties",
        "Number of Records",
        "Number of vehicles involved",
    ]

    for col in numeric_cols:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")

    return out


def make_analysis_ready(df: pd.DataFrame) -> pd.DataFrame:
    """Create a cleaned analysis frame with severity score."""
    out = df.drop_duplicates().copy()

    cat_cols = out.select_dtypes(include=["object"]).columns
    for col in cat_cols:
        out[col] = out[col].fillna("Unknown")

    severity_map = {
        "Slight Injury": 1,
        "Serious Injury": 2,
        "Fatal injury": 3,
    }

    if "Accident severity" in out.columns:
        out["severity_score"] = out["Accident severity"].map(severity_map)

    return out

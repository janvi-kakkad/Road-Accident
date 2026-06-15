from __future__ import annotations

import pandas as pd


def severity_distribution(df: pd.DataFrame) -> pd.DataFrame:
    """Return accident severity distribution."""
    if "Accident severity" not in df.columns:
        return pd.DataFrame(columns=["Accident severity", "accident_count"])

    return (
        df.groupby("Accident severity", dropna=False)
        .size()
        .reset_index(name="accident_count")
        .sort_values("accident_count", ascending=False)
    )


def severity_by_day(df: pd.DataFrame) -> pd.DataFrame:
    """Return day-wise severity trend table."""
    required = {"Day of week", "Accident severity"}
    if not required.issubset(df.columns):
        return pd.DataFrame(columns=["Day of week", "Accident severity", "accident_count"])

    return (
        df.groupby(["Day of week", "Accident severity"], dropna=False)
        .size()
        .reset_index(name="accident_count")
    )


def severity_by_hour(df: pd.DataFrame) -> pd.DataFrame:
    """Return hour-wise severity trend table."""
    required = {"hour_final", "Accident severity"}
    if not required.issubset(df.columns):
        return pd.DataFrame(columns=["hour_final", "Accident severity", "accident_count"])

    return (
        df.groupby(["hour_final", "Accident severity"], dropna=False)
        .size()
        .reset_index(name="accident_count")
        .sort_values("hour_final")
    )


def severity_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """Return area-wise severity table."""
    required = {"Area accident occured", "Accident severity"}
    if not required.issubset(df.columns):
        return pd.DataFrame(columns=["Area accident occured", "Accident severity", "accident_count"])

    return (
        df.groupby(["Area accident occured", "Accident severity"], dropna=False)
        .size()
        .reset_index(name="accident_count")
        .sort_values("accident_count", ascending=False)
    )


def hotspot_area_junction(df: pd.DataFrame) -> pd.DataFrame:
    """Return hotspot summary by area and junction."""
    required = {"Area accident occured", "Types of Junction"}
    if not required.issubset(df.columns):
        return pd.DataFrame(columns=["Area accident occured", "Types of Junction", "accident_count"])

    return (
        df.groupby(["Area accident occured", "Types of Junction"], dropna=False)
        .size()
        .reset_index(name="accident_count")
        .sort_values("accident_count", ascending=False)
    )


def cause_severity(df: pd.DataFrame) -> pd.DataFrame:
    """Return severity counts by cause of accident."""
    required = {"Cause of accident", "Accident severity"}
    if not required.issubset(df.columns):
        return pd.DataFrame(columns=["Cause of accident", "Accident severity", "accident_count"])

    return (
        df.groupby(["Cause of accident", "Accident severity"], dropna=False)
        .size()
        .reset_index(name="accident_count")
        .sort_values("accident_count", ascending=False)
    )

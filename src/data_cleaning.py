from __future__ import annotations

import pandas as pd
import numpy as np


def standardise_text(series: pd.Series) -> pd.Series:
    """Trim whitespace and standardise simple categorical labels."""
    return (
        series.astype("string")
        .str.strip()
        .str.title()
    )


def cap_outliers_iqr(
    series: pd.Series,
    multiplier: float = 1.5
) -> pd.Series:
    """Winsorise a numeric series using IQR fences."""
    clean = pd.to_numeric(series, errors="coerce")
    q1 = clean.quantile(0.25)
    q3 = clean.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - multiplier * iqr
    upper = q3 + multiplier * iqr
    return clean.clip(lower=lower, upper=upper)


def clean_operations_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply reproducible cleaning rules to the portfolio dataset."""
    out = df.copy()

    out = out.drop_duplicates(subset=["transaction_id"], keep="first")

    out["date"] = pd.to_datetime(out["date"], errors="coerce")

    for col in ["product", "region", "channel"]:
        out[col] = standardise_text(out[col])

    # Missing categorical region becomes explicitly visible rather than guessed.
    out["region"] = out["region"].fillna("Unknown")

    # Numeric imputation uses median as a simple portfolio approach.
    out["customer_satisfaction"] = pd.to_numeric(
        out["customer_satisfaction"], errors="coerce"
    )
    out["customer_satisfaction"] = out["customer_satisfaction"].fillna(
        out["customer_satisfaction"].median()
    )

    out["lead_time_days"] = pd.to_numeric(
        out["lead_time_days"], errors="coerce"
    )
    out["lead_time_days"] = out["lead_time_days"].fillna(
        out["lead_time_days"].median()
    )

    # Cap extreme quantity outliers while retaining records.
    out["units_clean"] = cap_outliers_iqr(out["units"])

    out["gross_revenue_clean_gbp"] = (
        out["units_clean"] * out["unit_price_gbp"]
    ).round(2)

    out["net_revenue_clean_gbp"] = (
        out["gross_revenue_clean_gbp"] * (1 - out["discount_pct"])
    ).round(2)

    out["year"] = out["date"].dt.year
    out["month"] = out["date"].dt.to_period("M").astype("string")
    out["quarter"] = "Q" + out["date"].dt.quarter.astype("Int64").astype("string")

    return out

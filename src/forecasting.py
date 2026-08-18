from __future__ import annotations

import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing


def build_monthly_revenue(df: pd.DataFrame) -> pd.Series:
    data = df.copy()
    data["date"] = pd.to_datetime(data["date"])
    monthly = (
        data.set_index("date")["net_revenue_clean_gbp"]
        .resample("MS")
        .sum()
        .asfreq("MS")
        .fillna(0)
    )
    return monthly


def forecast_revenue(
    series: pd.Series,
    periods: int = 3
) -> pd.DataFrame:
    """
    Basic portfolio forecast using Holt-Winters.

    This demonstrates forecasting workflow; it is not presented as a
    production planning model.
    """
    model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal="add",
        seasonal_periods=12,
        initialization_method="estimated",
    )
    fitted = model.fit(optimized=True)
    forecast = fitted.forecast(periods)

    return pd.DataFrame({
        "month": forecast.index,
        "forecast_revenue_gbp": forecast.values
    })

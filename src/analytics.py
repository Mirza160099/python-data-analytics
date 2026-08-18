from __future__ import annotations

import pandas as pd
import numpy as np


def kpi_summary(df: pd.DataFrame) -> dict:
    revenue = df["net_revenue_clean_gbp"].sum()
    profit = df["profit_gbp"].sum()
    orders = df["transaction_id"].nunique()
    units = df["units_clean"].sum()

    return {
        "revenue_gbp": round(float(revenue), 2),
        "profit_gbp": round(float(profit), 2),
        "profit_margin_pct": round(float(profit / revenue * 100), 2) if revenue else 0,
        "transactions": int(orders),
        "units": round(float(units), 2),
        "avg_order_value_gbp": round(float(revenue / orders), 2) if orders else 0,
        "avg_customer_satisfaction": round(float(df["customer_satisfaction"].mean()), 2),
        "avg_delivery_delay_days": round(float(df["delivery_delay_days"].mean()), 2),
    }


def revenue_by_dimension(df: pd.DataFrame, dimension: str) -> pd.DataFrame:
    return (
        df.groupby(dimension, dropna=False)
        .agg(
            revenue_gbp=("net_revenue_clean_gbp", "sum"),
            profit_gbp=("profit_gbp", "sum"),
            transactions=("transaction_id", "nunique"),
            units=("units_clean", "sum"),
        )
        .reset_index()
        .sort_values("revenue_gbp", ascending=False)
    )


def monthly_summary(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("month")
        .agg(
            revenue_gbp=("net_revenue_clean_gbp", "sum"),
            profit_gbp=("profit_gbp", "sum"),
            units=("units_clean", "sum"),
            transactions=("transaction_id", "nunique"),
        )
        .reset_index()
        .sort_values("month")
    )


def statistical_summary(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "units_clean",
        "discount_pct",
        "net_revenue_clean_gbp",
        "profit_gbp",
        "inventory_on_hand",
        "lead_time_days",
        "customer_satisfaction",
        "delivery_delay_days",
    ]
    return df[cols].describe().T.reset_index(names="metric")


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "units_clean",
        "discount_pct",
        "net_revenue_clean_gbp",
        "profit_gbp",
        "inventory_on_hand",
        "lead_time_days",
        "customer_satisfaction",
        "delivery_delay_days",
    ]
    return df[cols].corr(numeric_only=True)

from pathlib import Path
import json
import pandas as pd

from data_cleaning import clean_operations_data
from analytics import (
    kpi_summary,
    revenue_by_dimension,
    monthly_summary,
    statistical_summary,
    correlation_matrix,
)
from forecasting import build_monthly_revenue, forecast_revenue

RAW = Path("data/raw/operations_analytics_synthetic.csv")
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(RAW)

clean = clean_operations_data(df)
clean.to_csv(OUT / "operations_clean.csv", index=False)

kpis = kpi_summary(clean)
(OUT / "kpi_summary.json").write_text(json.dumps(kpis, indent=2))

for dimension in ["region", "product", "channel"]:
    revenue_by_dimension(clean, dimension).to_csv(
        OUT / f"revenue_by_{dimension}.csv", index=False
    )

monthly = monthly_summary(clean)
monthly.to_csv(OUT / "monthly_summary.csv", index=False)

statistical_summary(clean).to_csv(
    OUT / "statistical_summary.csv", index=False
)

correlation_matrix(clean).to_csv(
    OUT / "correlation_matrix.csv"
)

series = build_monthly_revenue(clean)
forecast = forecast_revenue(series, periods=3)
forecast.to_csv(OUT / "revenue_forecast_3m.csv", index=False)

print("Pipeline complete.")
print(json.dumps(kpis, indent=2))

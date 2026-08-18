# Python Data Analytics

A professional portfolio project demonstrating **Pandas, NumPy, data cleaning, exploratory analysis, reusable Python functions, statistical summaries, automation, forecasting basics and visualisation-ready outputs**.

> **Data note:** The dataset is fully synthetic and created specifically for this portfolio project.

## Why This Project Exists

Many analytics portfolios consist of one large Jupyter notebook.

This repository takes a more engineering-oriented approach:

- reusable functions
- separate cleaning and analytics modules
- automated pipeline execution
- documented methodology
- tests
- processed outputs
- forecasting component
- interview documentation

The goal is to show how Python analytics can become a **repeatable workflow**, not just an ad-hoc notebook.

## Business Scenario

The synthetic dataset represents operational sales activity across:

- products
- regions
- channels
- inventory
- lead times
- delivery performance
- customer satisfaction
- revenue and profit

Stakeholders want to understand:

- overall commercial performance
- product and regional performance
- operational service levels
- inventory patterns
- relationships between delay and satisfaction
- future revenue direction

## Tech Stack

- Python
- Pandas
- NumPy
- statsmodels
- pytest
- CSV / analytical data preparation

## Repository Structure

```text
python-data-analytics/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── data_cleaning.py
│   ├── analytics.py
│   ├── forecasting.py
│   └── run_pipeline.py
├── tests/
├── docs/
├── notebooks/
├── outputs/
├── screenshots/
├── requirements.txt
└── README.md
```

## Data Quality Challenges

The raw dataset intentionally includes:

- duplicate transaction IDs
- missing region values
- missing numeric values
- inconsistent categorical labels
- extreme quantity outliers

The project demonstrates reproducible handling rather than silently cleaning data.

See [`docs/data_quality.md`](docs/data_quality.md).

## Cleaning Functions

Examples include:

```python
standardise_text(series)
cap_outliers_iqr(series)
clean_operations_data(df)
```

The cleaning pipeline:

1. removes duplicate business keys
2. parses dates
3. standardises categorical labels
4. handles missing values
5. caps extreme quantity outliers
6. derives reporting fields

## Analytical Functions

Reusable functions provide:

- executive KPI summary
- grouped revenue analysis
- monthly trends
- descriptive statistics
- correlation matrix

Example:

```python
revenue_by_dimension(df, "region")
```

## Exploratory Data Analysis

The EDA framework covers:

- structure
- missing values
- duplicates
- numerical distributions
- categorical breakdowns
- correlations
- time trends
- business questions

See [`docs/eda_guide.md`](docs/eda_guide.md).

## Statistical Summaries

The pipeline generates descriptive statistics for:

- units
- discounts
- revenue
- profit
- inventory
- lead time
- satisfaction
- delivery delay

It also creates a correlation matrix for exploratory analysis.

> Correlation is treated as an exploratory relationship, not evidence of causation.

## Forecasting Basics

A Holt-Winters / Exponential Smoothing example demonstrates:

```text
Daily Transactions
       ↓
Monthly Revenue
       ↓
Trend + Seasonality
       ↓
3-Month Forecast
```

This is a learning example rather than a production demand forecast.

See [`docs/forecasting_basics.md`](docs/forecasting_basics.md).

## Automation

Run the full workflow:

```bash
pip install -r requirements.txt
python src/run_pipeline.py
```

Outputs include:

- cleaned dataset
- KPI summary
- revenue by region
- revenue by product
- revenue by channel
- monthly performance
- descriptive statistics
- correlation matrix
- basic revenue forecast

See [`docs/automation.md`](docs/automation.md).

## Testing

Run:

```bash
pytest
```

The included tests demonstrate that reusable analytics functions can be validated rather than treated as untestable notebook code.

## Visualisation-Ready Outputs

Processed files are designed for downstream use in:

- Power BI
- Tableau
- Excel
- Python visualisation

See [`docs/visualisation_outputs.md`](docs/visualisation_outputs.md).

## Skills Demonstrated

- Python
- Pandas
- NumPy
- Data cleaning
- Data validation
- Exploratory data analysis
- Descriptive statistics
- Correlation analysis
- Reusable functions
- Automation
- Time-series aggregation
- Forecasting basics
- Testing
- BI-ready data preparation
- Business analytics

## Interview Talking Points

1. `merge` vs `concat`.
2. `.loc` vs `.iloc`.
3. Pandas `groupby`.
4. Missing-value handling.
5. Outlier detection.
6. Vectorisation.
7. NumPy arrays.
8. Correlation vs causation.
9. Resampling time series.
10. Forecast validation.
11. Reusable functions.
12. Turning a notebook into a production-style pipeline.

## Portfolio Classification

**Type:** Portfolio Build  
**Data:** Synthetic  
**Purpose:** Demonstrate professional Python analytics foundations and interview readiness.

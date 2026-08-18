# Interview Case Study

## Situation
An operational dataset contains inconsistent categories, missing values, duplicates and outliers, while stakeholders need reliable performance reporting and a basic forward-looking view.

## Task
Build a reproducible Python analytics pipeline that cleans the data, performs EDA, produces reusable business summaries and demonstrates introductory forecasting.

## Action
- Created a synthetic operations dataset with realistic data-quality issues.
- Built reusable Pandas functions for text cleaning, missing-value handling and IQR outlier capping.
- Created analytical functions for KPIs, grouped summaries, descriptive statistics and correlations.
- Automated generation of visualisation-ready CSV outputs.
- Added Holt-Winters forecasting as a basic time-series example.
- Added simple pytest tests for cleaning functions.
- Documented cleaning decisions, EDA workflow, forecasting limitations and production extensions.

## Result
Produced a recruiter-facing Python analytics repository showing code organisation, data preparation, reusable analysis, automation, statistics and forecasting fundamentals rather than relying on a single notebook.

## Interview Talking Points
1. Pandas `groupby`.
2. `merge` vs `concat`.
3. Missing-value strategies.
4. Outlier handling.
5. Vectorisation vs loops.
6. `apply` trade-offs.
7. `loc` vs `iloc`.
8. Descriptive statistics.
9. Correlation vs causation.
10. Time-series resampling.
11. Forecast validation.
12. How to productionise a Python analytics script.

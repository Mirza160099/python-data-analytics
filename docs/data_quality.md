# Data Quality Strategy

The raw synthetic dataset intentionally contains:
- duplicate transaction IDs
- missing values
- inconsistent text casing / whitespace
- extreme quantity outliers

## Cleaning Decisions

### Duplicates
Deduplicate on `transaction_id`.

### Missing Region
Use `Unknown` rather than inventing a country.

### Missing Numeric Values
Median imputation is used as a simple portfolio method.

Production treatment should depend on:
- missingness mechanism
- business meaning
- model/report sensitivity

### Text Standardisation
Strip whitespace and standardise case.

### Outliers
Extreme quantity values are capped using IQR-based winsorisation.

This keeps the row while limiting unrealistic distortion.

## Principle
Cleaning rules should be:
- explicit
- reproducible
- documented
- testable
- appropriate to the business context

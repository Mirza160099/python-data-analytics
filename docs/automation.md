# Automation Design

The reusable pipeline is:

```text
Raw CSV
   |
   v
Cleaning Functions
   |
   v
Clean Dataset
   |
   +--> KPI JSON
   +--> Region Summary
   +--> Product Summary
   +--> Channel Summary
   +--> Monthly Summary
   +--> Statistical Summary
   +--> Correlation Matrix
   +--> 3-Month Forecast
```

`src/run_pipeline.py` creates all outputs from the raw file.

## Production Extensions

A production version could add:
- scheduled orchestration
- API/database ingestion
- schema validation
- logging
- exception handling
- data-quality alerts
- unit/integration tests
- cloud storage
- warehouse loading
- Power BI/Tableau refresh

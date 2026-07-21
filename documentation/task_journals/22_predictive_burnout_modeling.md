# Task Journal: Predictive Burnout Modeling

## Item Details
- **ID:** 22
- **Description:** Use the `data_analyst` skill principles (scikit-learn pipelines, fixed random seeds) to build a machine learning model that predicts burnout risk based on interruption frequency and sustained high-workload periods.
- **Context:** Adds predictive value rather than just historical reporting.

## Delegations
1. **Model:** subagent (pro)
   **Brief:** Build a machine learning pipeline using `scikit-learn` in `scripts/predict_burnout.py` (or similar). Follow `data_analyst` principles: fixed random seeds (`random_state=42`), pipeline (`sklearn.pipeline.Pipeline`), and generate predictive metrics (e.g., burnout risk) based on features like interruption frequency and workload periods, then output these metrics as part of the data ingestion pipeline (e.g., updating `pizza_metrics.json` via `etl.py` or separate pipeline). Add unit tests.
   **Outcome:** Pending

## Next Step
- Wait for subagent to implement the model and update the data pipeline.

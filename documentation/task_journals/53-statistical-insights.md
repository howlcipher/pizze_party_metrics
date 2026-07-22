# UI/UX: Add Statistical Insights / Correlations Card (#53)

## Status: In Progress
## Next Step: Evaluate agy implementation of the card and review diff.

## Context
Add a "Key Takeaways" component highlighting the strong statistical correlations (e.g., 96.8% inverse correlation between meetings and Pizza Party Index). Sourced from `advanced_collaboration_insights.json` (`correlations`), providing hard analytical context to the dashboard.

## Delegations
1. **Model**: gemini-3.1-pro-high (via agy)
   **Brief**: Implement `StatisticalInsightsCard.tsx` component in `src/components/Charts/` that reads `src/data/advanced_collaboration_insights.json`'s `correlations` field. Display the inverse correlation between meetings and Pizza Party Index (96.8%), and other key takeaways. Then lazy load and add it to `src/components/Dashboard.tsx`.
   **Outcome**: Pending

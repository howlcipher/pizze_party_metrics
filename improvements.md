# 🚀 Improvement Backlog

This document is the authoritative, ranked backlog for the Pizza Party Metrics project.

## Working Protocol

1. **Open a task journal.** Update it and commit at every milestone.
2. **Re-evaluate the model.** Pick the least expensive available model that can do the job well.
3. **Route the crafted skills.** Check the skills manifest for skills matching the task.
4. **Scan for helpful free tools.** Consider whether a free or open source tool would materially improve the work.
5. **Finish the loop.** Every code change ships with relevant automated tests. Verify the change works end to end, commit, and push.

## Ranked Backlog (best ROI first)

Pending rows are ranked by a diminishing-returns score, recomputed at every groom:

**Score = (Value × Decay) ÷ Effort**

- **Value (1–8):** pain or risk removed if the item ships.
- **Decay:** geometric halving per already-shipped item in the same theme (1.0 → 0.5 → 0.25 …).
- **Effort (1–8):** roughly log-scale; 1 = minutes, 8 = weeks.
- **ROI floor = 0.5:** items scoring below the floor stay open but are flagged ⚠️.

| # | Improvement | Status | Score (V×D÷E) | Claude model | Gemini model | ROI rationale |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Agent Suggestion] Frontend: Rendering Efficiency (useMemo) | Pending | 4.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Major performance fix) * 1.0 / 2 (Simple hook) = 4.0 |
| 2 | [Agent Suggestion] DevOps: Enforce Strict Dependency Versioning and Enable Caching | Pending | 3.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Fixes flakey builds) * 1.0 / 2 (1-line action fix) = 3.5 |
| 3 | [Agent Suggestion] UI/UX: Reset Filters CTA | Pending | 3.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Saves users from dead ends) * 1.0 / 2 (Simple button) = 3.5 |
| 4 | [Agent Suggestion] Data Pipeline: Add Module-Level Documentation & Decouple Configuration | Pending | 3.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (Good code hygiene) * 1.0 / 2 (Simple variable moves) = 3.0 |
| 5 | [Agent Suggestion] Accessibility: Form Control Association & ARIA charts | Pending | 2.66 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Compliance issue) * 1.0 / 3 (Template updates) = 2.66 |
| 6 | [Agent Suggestion] Data Pipeline: Defensive Network Requests & Error Handling | Pending | 2.66 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Prevents crashes) * 1.0 / 3 (Try-except & timeouts) = 2.66 |
| 7 | [Agent Suggestion] DevOps: Implement Multi-Stage Job Separation with Quality & Security Gates | Pending | 2.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Security & CI integrity) * 1.0 / 4 (Workflow refactor) = 2.0 |
| 8 | Theme Options: Light, Dark, and Color-blind Modes | Pending | 1.75 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (high accessibility/UX value) * 1.0 / 4 (standard UI state management) = 1.75 |
| 9 | [Agent Suggestion] DevOps: Isolate ETL Data Pipeline and Ensure Idempotency | Pending | 1.75 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Decouples failure modes) * 1.0 / 4 (Artifact passing setup) = 1.75 |
| 10 | [Agent Suggestion] Data Pipeline: Vectorize Pandas Operations | Pending | 1.75 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Idiomatic & fast) * 1.0 / 4 (Logic rewrite) = 1.75 |
| 11 | Live Data Ingestion API / Backend | Pending | 1.33 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Core requirement for live data) * 1.0 / 6 (Significant backend work) = 1.33 |
| 12 | Stereotype Pizza Parlor Aesthetic Overhaul | Pending | 1.20 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (fun brand alignment) * 1.0 / 5 (significant CSS/UI redesign) = 1.20 |
| 13 | [Agent Suggestion] Meeting vs. Maker Time Analysis | Pending | 0.88 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Actionable insight) * 0.5 (decay from Demographic Analytics) / 4 = 0.88 |
| 14 | Interruption & Context Switch Impact Dashboard | Pending | 0.80 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (High value for productivity insights) * 0.5 (decay) / 5 = 0.80 |
| 15 | [Agent Suggestion] Predictive Burnout Modeling | Pending | 0.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (Advanced ML feature) * 0.5 (decay) / 6 = 0.50 |
| 16 | Demographic Analytics (Age, Industry, Gender) | Done (2026-07-21) | - | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | Shipped! |

## Details

### 1. [Agent Suggestion] Frontend: Rendering Efficiency (useMemo)
**Description:** Extract the unique options lists (industries, ageGroups, workSetups) into a `useMemo` hook in `PizzaBoxFilter.jsx` to prevent calculating a 100KB dataset on every re-render.
**Context:** Based on the `frontend_engineering` skill. Currently recalculates `[...new Set(...)]` on every re-render, creating severe UI lag.

### 2. [Agent Suggestion] DevOps: Enforce Strict Dependency Versioning and Enable Caching
**Description:** Update `deploy.yml` to use `npm ci` exclusively and enable caching for both `setup-python` (`cache: 'pip'`) and `setup-node` (`cache: 'npm'`).
**Context:** Based on the `devops` skill. Prevents unverified versions from breaking builds and improves speed.

### 3. [Agent Suggestion] UI/UX: Reset Filters CTA
**Description:** Add a "Reset Filters" CTA button when a combination of filters yields no results ("No slices left!").
**Context:** Based on the `ui_ux` skill to reduce friction and cognitive load for the user trying to exit a dead-end state.

### 4. [Agent Suggestion] Data Pipeline: Add Module-Level Documentation & Decouple Configuration
**Description:** Add a structured module-level docstring to `etl.py` and move hardcoded URLs to top-level constants.
**Context:** Enforces `data_analyst` reporting standards and `software_development` low coupling principles.

### 5. [Agent Suggestion] Accessibility: Form Control Association & ARIA charts
**Description:** Map `<label>` elements to `<select>` tags using `htmlFor` and `id`. Add `.sr-only` descriptions or `aria-labels` to the Recharts graphics.
**Context:** Based on the `accessibility` skill for WCAG compliance.

### 6. [Agent Suggestion] Data Pipeline: Defensive Network Requests & Error Handling
**Description:** Wrap all API and download calls (`requests.get`) in `etl.py` with explicit `timeout=15` settings and `try...except` blocks emitting structured JSON logs.
**Context:** Enforces `software_development` guidelines for strict error handling and resilience.

### 7. [Agent Suggestion] DevOps: Implement Multi-Stage Job Separation with Quality & Security Gates
**Description:** Split the monolithic `build-and-deploy` job in `deploy.yml` into `validate`, `build`, and `deploy` jobs with security scanning (Trivy/npm audit).
**Context:** Aligns with `devops` constraints ensuring security and logical environment isolation.

### 8. Theme Options: Light, Dark, and Color-blind Modes
**Description:** Add a theme switcher that allows users to toggle between Light Mode, Dark Mode (currently default), and a Color-blind friendly mode.
**Context:** This improves accessibility (see `accessibility` skill) and gives users control over their dashboard viewing experience.

### 9. [Agent Suggestion] DevOps: Isolate ETL Data Pipeline and Ensure Idempotency
**Description:** Extract the Python ETL script to its own `data-pipeline` GitHub Actions job and pass the JSON artifact to the `build` job.
**Context:** Ensures absolute separation between the Python execution environment and Node.js build per `devops_sre` standards.

### 10. [Agent Suggestion] Data Pipeline: Vectorize Pandas Operations
**Description:** Refactor the `process_data` function in `etl.py` to use vectorized pandas operations instead of iterating with `.iloc[0]`.
**Context:** Adheres to `data_analyst` principles for optimal DataFrame performance and readability.

### 11. Live Data Ingestion API / Backend
**Description:** Build a backend or integration layer (e.g., WebSockets or a polling API) to ingest real and live data for the dashboard, replacing any static or mocked data.
**Context:** Required to fulfill the "real and live data" mandate.

### 12. Stereotype Pizza Parlor Aesthetic Overhaul
**Description:** Redesign the dashboard to lean heavily into a stereotypical pizza parlor theme. Think red and white checkered tablecloth patterns, Italian flag color accents (green/red/white), and rustic UI elements.
**Context:** A fun branding exercise that gives the dashboard a unique identity compared to generic SaaS dashboards.

### 13. [Agent Suggestion] Meeting vs. Maker Time Analysis
**Description:** Analyze calendar data to show the ratio of uninterrupted "Maker Time" versus fragmented "Meeting Time."
**Context:** A natural extension to the context-switching metrics that provides highly actionable insights for teams.

### 14. Interruption & Context Switch Impact Dashboard
**Description:** Visualize how interruptions destroy context switching. We need to track the frequency of interruptions (e.g., Slack messages, ad-hoc calls) and correlate them with task completion times or velocity drops.
**Context:** This requires tracking the "cost" of a context switch. As defined by the product strategy (MVP), we should start with a simple time-loss calculation before moving to complex models.

### 15. [Agent Suggestion] Predictive Burnout Modeling
**Description:** Use the `data_analyst` skill principles (scikit-learn pipelines, fixed random seeds) to build a machine learning model that predicts burnout risk based on interruption frequency and sustained high-workload periods.
**Context:** Adds predictive value rather than just historical reporting.

### 16. Demographic Analytics (Age, Industry, Gender)
**Description:** Add demographic breakdowns to the metrics. Understand how different age ranges, industries, and genders interact with the product or experience different levels of productivity.
**Context:** Ensure data pipelines aggregate this securely and anonymized. 
**Done note (2026-07-21):** Implemented new UI components using Recharts for Age and Gender breakdowns. Data structure updated to support these dimensions, and the dashboard aesthetic upgraded to dark mode.

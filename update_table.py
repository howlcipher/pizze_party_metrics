import re

with open('improvements.md', 'r') as f:
    content = f.read()

new_table = """| # | Improvement | Status | Score (V×D÷E) | Claude model | Gemini model | ROI rationale |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | [Agent Suggestion] Frontend: Rendering Efficiency (useMemo) | Done (2026-07-21) | 4.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Major performance fix) * 1.0 / 2 = 4.00 |
| 2 | [Agent Suggestion] DevOps: Enforce Strict Dependency Versioning and Enable Caching | Done (2026-07-21) | 3.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Fixes flakey builds) * 1.0 / 2 = 3.50 |
| 4 | [Agent Suggestion] Data Transparency: Raw Data Export & Reproducibility | Done (2026-07-21) | 3.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Ensures reproducibility) * 1.0 / 2 = 3.50 |
| 23 | Demographic Analytics (Age, Industry, Gender) | Done (2026-07-21) | - | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | Shipped! |
| 3 | [Agent Suggestion] UI/UX: Reset Filters CTA | Pending | 3.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Saves users from dead ends) * 1.0 / 2 = 3.50 |
| 5 | [Agent Suggestion] Data Pipeline: Add Module-Level Documentation & Decouple Configuration | Pending | 3.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (Good code hygiene) * 1.0 / 2 = 3.00 |
| 6 | [Agent Suggestion] Accessibility: Form Control Association & ARIA charts | Pending | 2.66 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Compliance issue) * 1.0 / 3 = 2.66 |
| 7 | [Agent Suggestion] Data Pipeline: Defensive Network Requests & Error Handling | Pending | 2.66 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Prevents crashes) * 1.0 / 3 = 2.66 |
| 9 | [Agent Suggestion] Data Pipeline: Ingestion Layer Quality Checks | Pending | 2.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Stops bad pipelines) * 1.0 / 4 = 2.00 |
| 10 | [Agent Suggestion] Data Pipeline: Vectorize Pandas Operations | Pending | 1.75 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Idiomatic & fast) * 1.0 / 4 = 1.75 |
| 17 | Theme Options: Light, Dark, and Color-blind Modes | Pending | 1.75 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (high UX value) * 1.0 / 4 = 1.75 |
| 12 | [Agent Suggestion] Data Pipeline: Real GitHub Collaboration Data Integration | Pending | 1.60 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Mandate for real data) * 1.0 / 5 = 1.60 |
| 8 | [Agent Suggestion] Data Transparency: Analytics Methodology Page | Pending | 1.33 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Addresses data trust) * 0.5 (decay) / 3 = 1.33 |
| 14 | Live Data Ingestion API / Backend | Pending | 1.33 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Core requirement) * 1.0 / 6 = 1.33 |
| 21 | Stereotype Pizza Parlor Aesthetic Overhaul | Pending | 1.20 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (Fun branding) * 1.0 / 5 = 1.20 |
| 16 | [Agent Suggestion] DevOps: Implement Multi-Stage Job Separation with Quality & Security Gates | Pending | 1.00 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Security) * 0.5 (decay) / 4 = 1.00 |
| 18 | [Agent Suggestion] DevOps: Isolate ETL Data Pipeline and Ensure Idempotency | Pending | 0.88 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Decouples failure) * 0.5 (decay) / 4 = 0.88 |
| 19 | [Agent Suggestion] Meeting vs. Maker Time Analysis | Pending | 0.88 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Actionable insight) * 0.5 (decay) / 4 = 0.88 |
| 11 | [Agent Suggestion] Async Collaboration Velocity Metric | Pending | 0.80 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (Proves thesis) * 0.5 (decay) / 5 = 0.80 |
| 20 | Interruption & Context Switch Impact Dashboard | Pending | 0.80 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 8 (High value) * 0.5 (decay) / 5 = 0.80 |
| 13 | [Agent Suggestion] Documentation & Knowledge Transfer Health | Pending | 0.70 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Strong proxy for collab) * 0.5 (decay) / 5 = 0.70 |
| 15 | [Agent Suggestion] Cross-Time-Zone Collaboration Index | Pending | 0.58 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 7 (Remote advantage) * 0.5 (decay) / 6 = 0.58 |
| 22 | [Agent Suggestion] Predictive Burnout Modeling | Pending | 0.50 | claude-3-7-sonnet-20250219 | gemini-3.1-pro-high | 6 (Advanced ML) * 0.5 (decay) / 6 = 0.50 |"""

new_content = re.sub(r'\| # \| Improvement \| Status \|.*?\| 23 \| Demographic Analytics.*?Shipped! \|', new_table, content, flags=re.DOTALL)

with open('improvements.md', 'w') as f:
    f.write(new_content)

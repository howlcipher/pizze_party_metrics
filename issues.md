# 🐛 Bug Backlog

This document is the authoritative, ranked backlog for known flaws, bugs, and broken items in the Pizza Party Metrics project. It mirrors the structure of `improvements.md`.

## Ranked Backlog (best ROI first)

Pending bugs carry a diminishing-returns score (Score = Value × Decay ÷ Effort, ROI floor 0.5). When a new bug is found, add a row here and a matching detail section below, then work the table top down.

| # | Bug | Status | Score (V×D÷E) | Claude model | Gemini model | ROI rationale |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | GitHub Pages deployment displays a white blank page | Done (2026-07-21) | 8.0 | claude-3-7-sonnet-20250219 | gemini-2.5-pro | 8 (broken core functionality) * 1.0 (no decay) / 1 (likely simple path or build error) = 8.0 |

## Details

### 1. GitHub Pages deployment displays a white blank page
**Description:** The production deployment at `https://howlcipher.github.io/pizze_party_metrics/` is currently showing a blank white screen instead of rendering the React application.
**Context:** The `vite.config.js` currently sets `base: '/pizze_party_metrics/'`. Need to investigate whether the assets are failing to load (404s due to base path mismatch) or if there's a runtime JavaScript error in production (e.g., related to React or Vite configuration).
**Done note (2026-07-21):** Created `public/.nojekyll` to prevent GitHub Pages (Jekyll) from ignoring Vite's `_assets` directory.

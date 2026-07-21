# Durable Knowledge

This document stores durable knowledge from agent sessions so that technical decisions, workarounds, and environment facts survive outside any one agent's memory.

## Deployment

### GitHub Pages & Vite
- **The Issue:** Vite builds output an `assets` directory which can sometimes be named `_assets`. GitHub Pages uses Jekyll by default, and Jekyll ignores any directories or files that start with an underscore (`_`), causing the main JavaScript and CSS files to return a 404 error (resulting in a blank white page).
- **The Fix:** Create an empty `public/.nojekyll` file in the Vite project. This disables Jekyll processing on GitHub Pages entirely and ensures that all Vite assets are served correctly.
- **Reference:** Fixed in `/pizza_party_metrics/issues.md` on 2026-07-21.

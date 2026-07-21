# Frontend & Deployment Gotchas

This document captures durable knowledge and troubleshooting steps from past sessions, particularly around Vite and GitHub Pages deployments.

## Vite & GitHub Pages

### 1. The "White Blank Page" Issue
When deploying a Vite React app to GitHub Pages, the site might load as a blank white page.
**Cause:** GitHub Pages uses Jekyll by default. Jekyll ignores folders starting with an underscore (like Vite's default `_assets` directory).
**Solution:** Create an empty file named `.nojekyll` in the `public/` directory before building. This instructs GitHub Pages to bypass Jekyll processing and serve the `_assets` folder correctly.

### 2. Favicon Not Updating (Cache Issues)
After replacing `favicon.svg` in the `public/` directory, the browser may still show the default Vite logo.
**Cause:** Browsers aggressively cache favicons, and Vite's default setup may lack fallback support for older browsers.
**Solution:**
1. **Cache Busting:** Add a query parameter to the `href` in `index.html`, e.g., `<link rel="icon" type="image/svg+xml" href="/favicon.svg?v=2" />`.
2. **Fallback Icon:** Generate a `favicon.ico` using tools like ImageMagick and add it to `public/`.
3. **Alternate Link:** Add `<link rel="alternate icon" href="/favicon.ico" />` in `index.html` to ensure all browsers correctly load the custom icon instead of falling back to default or cached ones.

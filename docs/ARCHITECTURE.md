# Architecture

## Data flow
`pipeline/fetch.py` downloads the pinned official June 2026 Field of Study and Institution ZIPs. It validates SHA-256 hashes from the shipped manifest, extracts only CSVs, and avoids ZIP path traversal by retaining only basenames.

`pipeline/train.py` reads program-level public data and joins institution state by UNITID (many-to-one validated). It coerces published numeric outcomes separately from `PS`, ordinary missing values and other non-numeric states. It creates a program-family key, OPEID6 × CIPCODE × CREDLEV, to keep branch-pooled outcomes within one split. It selects a main-campus representative where available. It does not attempt to reconstruct hidden outcomes.

Three LightGBM models fit quantiles 0.1, 0.5 and 0.9, with 350 boosting iterations, 23 leaves, minimum 35 child samples, learning rate .045 and L2 regularization 2. Seeds 42/43 fix institution-grouped splits. Quantile crossings are sorted before interval calibration. Calibration uses `max(lower-y, y-upper, 0)` and a finite-sample 80% quantile, separately by completion-size band where n≥100; smaller bands use a global correction. Lower bounds are clipped at zero.

Test labels are never used for fitting or calibration. Results are exported for all source records, but the UI only receives estimates for suppressed programs with at least 30 matching field/credential training outcomes. Public official earnings are always preferred. Precomputation keeps browser deployment lightweight and keyless.

## Browser
- `src/domain.ts`: data types, tuple decoding, safe export, search normalization, fixed-payment formula and interval comparisons.
- `src/main.ts`: explicit UI state, three views, async state-file caching, request-generation guards, search, comparison and data visualization.
- `src/style.css`: responsive blush/plum visual system, self-hosted type, focus states and reduced-motion support.
- `public/data/`: school index, field/credential dictionaries, generated metrics and provenance, state-partitioned record arrays, reproducible sample for the opening visualization.

A school selection fetches just its state partition. A newer request supersedes an older request, preventing stale results from replacing a later selection. Network errors remain visible and retryable. CSV exports label every observation's source and quote cells; leading spreadsheet formula characters are prefixed.

## Privacy and persistence
No backend, no accounts, no hosted inference API, no cookies or telemetry. Search and hypothetical loan inputs are not submitted anywhere. Static-host access logs still belong to the hosting provider. Program links encode public identifiers only. Comparison pins exist only in page memory and are lost on reload.

## Deployment
GitHub Pages builds the Vite static output (`base: './'`). GitHub Actions runs frontend tests, an independent Python check of saved predictions, production compilation and browser journeys. Refreshing data is intentionally manual: a changing dataset must be reviewed and retrained, not silently swapped underneath frozen evaluation evidence.

## Trade-offs
The original plan proposed browser model inference and federal earnings thresholds. The shipped version uses auditable precomputed model outputs and an explicitly hypothetical benchmark. This avoids implying access to suppressed truth or a regulatory determination. There is no n8n workflow: no feature requires credentials, integration or scheduled collection.

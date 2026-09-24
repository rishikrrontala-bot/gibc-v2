# PROGRESS: Global Innovation Build Challenge V2

Running log for the unattended cloud build. A resumed session should read this first and continue from **Next up**.

**Deadline:** Thu Oct 1, 2026 · 11:45 AM EDT (`2026-10-01T11:45:00-04:00`)
**All deliverables done by:** Wed Sep 30, 2026 · 11:45 AM EDT (24 h buffer, CLAUDE.md lesson 2)

## Countdown log

| When (ET) | Hours to deadline | Phase |
|---|---|---|
| Wed Sep 23 · 10:35 PM | 181.2 h | 0: setup |
| Wed Sep 23 · 10:56 PM | 180.8 h | 1–3: research + concept done, pushed |
| Wed Sep 23 · 11:00 PM | 180.7 h | 4: design direction done, pushed |
| Wed Sep 23 · 11:03 PM | 180.7 h | **Paused at Rishik's request** (push everything and stop at 11:06 PM). Phase 5 not started in code |

## Phase plan (budgeted backwards from the 24 h buffer)

Working window: Wed Sep 23 10:35 PM → Wed Sep 30 11:45 AM ET ≈ **157 h**. More than 48 h remain, so research gets a full pass.

| # | Phase | Budget | Ends by (ET) |
|---|---|---|---|
| 0 | Setup, tool check, PROGRESS.md | 0.5 h | Wed Sep 23 11:15 PM |
| 1–2 | Research: verify event facts, 5–8 winner briefs, RESEARCH-BRIEF | 4 h | Thu Sep 24 3:30 AM |
| 3 | Concepts ×3 scored, pick, CONCEPT.md pushed | 1 h | Thu Sep 24 4:30 AM |
| 4 | Design direction (PRODUCT.md, DESIGN.md) | 2 h | Thu Sep 24 6:30 AM |
| 5 | Core build, wow moment first (~50 %) | 70 h | Sun Sep 27 4:30 AM |
| 6 | Quality passes (critique → audit → polish, live checks) | 12 h | Sun Sep 27 4:30 PM |
| 7 | Demo video (~20 %) | 20 h | Mon Sep 28 12:30 PM |
| 8 | Submission kit (~15 %) | 16 h | Tue Sep 29 4:30 AM |
| 9 | Ship to main, HANDOFF.md, buffer (~15 %) | 31 h | **Wed Sep 30 11:45 AM** |

Long-running compute (model training, if the concept needs it) runs in the background during phases 5–6, with checkpoints, so wall-clock training time overlaps the site build.

## Environment check (Wed Sep 23, 10:40 PM ET)

| Tool | Status |
|---|---|
| Node | v22.22.2, npm 10.9.7 |
| Python | 3.11.15 |
| Playwright Chromium | present at `/opt/pw-browsers` (chromium-1194) |
| ffmpeg | installed via `apt-get install ffmpeg` (6.1.1) |
| CPU | 4 vCPU Intel Xeon @ 2.8 GHz, AVX-512 (no AMX, no bf16), 15 GB RAM, no GPU |
| PyTorch | 2.14.0 installed from PyPI (download.pytorch.org is blocked) |
| n8n | `N8N_BASE_URL` is **unset**, so there is no API access. Any workflow ships as an importable `n8n/*.json` file |
| Design skills in session | `dataviz`, `ui-demo`, `make-interfaces-feel-better`, `accessibility` loaded. **Missing:** `impeccable`, `emil-design-skills:animate`, taste-skill, `hypersite`. Fallback used: cloned `pbakaus/impeccable`, `emilkowalski/skills`, `leonxlnx/taste-skill` into `/tmp/skills` and read their `SKILL.md` files directly |

### Network policy (important for a resumed session)
The environment is **not** on Full network access. Verified by probing:
- **Allowed:** `github.com` via git, `api.github.com`, `raw.githubusercontent.com`, `media.githubusercontent.com` (LFS), `registry.npmjs.org`, PyPI, `archive.ubuntu.com`, WebSearch.
- **Blocked (403 at the egress proxy):** `devpost.com` and every `*.devpost.com` page (WebFetch too), `huggingface.co`, `download.pytorch.org`, `youtube.com`, `wikipedia.org`, `archive.org`, `unpkg.com`, `cdn.jsdelivr.net`, Yahoo Finance, FRED, SEC, Kaggle, Gutenberg.
- Consequence for research: Devpost pages can't be opened directly. Winner verification uses search-engine results that quote the Devpost page plus the winner's GitHub repo cloned and read (anonymous git reads of public repos work). Each brief states exactly which of those checks passed.
- Consequence for data/models: no Hugging Face downloads. Data must come from GitHub, PyPI/npm packages, or be generated in-repo.

## Log

### Phase 0: setup (Wed Sep 23, 10:35 PM ET · 181.2 h left)
- Read CLAUDE.md, HACKATHON.md, PROMPT.md, hackathon-win SKILL.md + references + templates.
- Checked tools and network (above). Created this file.

### Phase 1–3: research and concept (Wed Sep 23, 10:40–10:56 PM ET · ~181 h left)
- HACKATHON.md re-verified via the search index (Devpost itself is blocked); new facts marked ✚.
- `research/winners/`: 6 briefs (CollegeTrue, FairLend, DebtShield, Anya [same Featherless prize], GridSense, AccessLens), sourced from HackWinnerDB with each repo cloned and read. GIBC V1 winners can't be verified from this network (see `research/winners/README.md`).
- `research/FIELD-SCAN.md`: live GIBC V2 competitors. Track 01 has ≥ 5 GPU-trained 49M models, which overturned the TECH hypothesis.
- `research/RESEARCH-BRIEF.md`, `research/CONCEPTS.md` (A Four Cores 2.04 · **B Withheld 4.65** · C Second Ask 3.45), `CONCEPT.md` pushed.
- Siblings re-checked at 10:55 PM: Low Sun, Zeer, In Its Place, Muslin, All the Way Down, Between Bells, Brackets. No overlap.

### Phase 4: design direction (Wed Sep 23, 10:57–11:00 PM ET)
- impeccable launcher ran from `/tmp/skills/impeccable/plugin/skills/impeccable/scripts/impeccable`. PRODUCT.md was written unattended, with inferred facts labelled (Rishik said he's unavailable, so no interview probe).
- `concept-seed` ran **degraded** (impeccable.style is blocked, so no challengers or QUALITY BAR boards). My 7 grounded candidates were Scantron sheet · W-2 drop-out form · NOAA hurricane cone · 1870s Statistical Atlas · redacted FOIA release · green-bar ledger printout · college-fair ephemera. Roll 1 assigned #5 (redaction); that was declined on product truth (it implies un-redaction). Re-roll 1 assigned **#6 green-bar printout**, which is the build direction.
- Direction contract: `.impeccable/surfaces/index-html.md`. Tokens and type (Public Sans / Martian Mono / Doto, all on npm @fontsource) in DESIGN.md, contrast computed.
- No image generation in this session, so the build is code-led.

## Resume notes (read these first if this session died)
- **Concept:** *Withheld* (Track 02 Applied: Finance). Estimate earnings (and debt) for the 77.7 % of College Scorecard programs whose figures are `PrivacySuppressed`, with split-conformal 80 % intervals calibrated by program-size band, and compare them to the federal earnings line (OBBBA "do no harm" test, STATS final rule of Jul 1 2026).
- **Data source that works from this VM:** `git clone --depth 1 --filter=blob:none --no-checkout https://github.com/Amherst-Statistics/CollegeScorecard`, then `git checkout HEAD -- inst/extdata/Most-Recent-Cohorts-Field-of-Study.csv.bz2 inst/extdata/Most-Recent-Cohorts-Institution.csv.bz2`. FoS: 233,979 rows × 160 cols; EARN_MDN_4YR published for 52,221; DEBT_ALL_STGP_EVAL_MDN for 48,143.
- The data dictionary lives in the `RTICWDT/college-scorecard` repo at `public/files/CollegeScorecardDataDictionary.xlsx` (git-cloneable).
- Still needed: per-state high-school earnings thresholds (search a GitHub mirror or the Federal Register via the search index; otherwise document the fallback, e.g. the `EARN_GT_THRESHOLD` share > 0.5).
- The research clones live in `/home/user/research-src` (not in the repo; re-clone if the VM is new).
- **Data vintage problem (found 11:02 PM):** the Amherst mirror's Field of Study file was last committed **2023-08-26** (commit `b490439`). It predates the May 2024 NULL→NA change and the June 2024 `EARN_MDN_5YR` columns, so it's a 2023 release. The official site says the data was last updated **June 10, 2026**. Earnings in our file: `EARN_MDN_4YR` = AY2014-15/2015-16 completers measured CY2019/2020 in 2021 dollars; debt `DEBT_ALL_STGP_EVAL_MDN` = pooled AY2018-19/2019-20.
- **Planned real fix (next step, not yet done):** add `.github/workflows/data-refresh.yml` (runs on push + a weekly cron + workflow_dispatch; `permissions: contents: write`). GitHub-hosted runners have open internet, so it downloads the current official `Most-Recent-Cohorts-Field-of-Study` and `Most-Recent-Cohorts-Institution` zips (find the links on https://collegescorecard.ed.gov/data/, where files are served from `ed-public-download.app.cloud.gov/downloads/…`), records SHA-256 + URL + download time in `manifest.json`, recompresses the CSVs as `.csv.xz`, and commits them to an orphan branch `data`. This VM then runs `git fetch origin data`. Fall back to the 2023 Amherst mirror only if that fails, and disclose the vintage either way. Actions cron replaces n8n for this schedule because it needs no secret (document that in ARCHITECTURE.md).
- **Facts from the official FoS documentation (Version: September 2025, in the RTICWDT repo at `public/files/FieldOfStudyDataDocumentation.pdf`) that matter for rigor and LIMITATIONS:** debt metrics use cell suppression with undisclosed rules. Earnings use **differentially private noise**; noisy medians with relative error above a threshold are suppressed. Published 1-yr medians are within 1 % of truth 50 % of the time and within 1–4 % 44 % of the time; the median absolute difference is $2,224 (1-yr) and $3,235 (5-yr). That's the irreducible noise floor to compare model error against. `EARN_GT_THRESHOLD_xYR` is a DP-noised **count** of graduates earning more than a high-school graduate (divide by `EARN_COUNT_WNE_xYR` for a share).
- Python deps installed on this VM: pandas 3.0.6, numpy 2.4.6, scikit-learn 1.9.1, lightgbm 4.7.0, openpyxl, pytest, torch 2.14.0; `poppler-utils` via apt (pypdf is broken here, so use `pdftotext`).

## Next up
- Phase 5a-0: the data-refresh workflow above (official June 2026 files via GitHub Actions → `data` branch).
- Phase 5a: `pipeline/` in Python: `fetch.py` (clone the Amherst mirror, verify SHA-256), `profile.py` (suppression stats → `data/profile.json`), `features.py`, `train.py` (quantile GBM + baselines, institution-grouped CV), `conformal.py` (Mondrian by size band), `export.py` (compact binary + JSON for the site), `tests/` with pytest.
- Phase 5b: Vite + TS site per the direction contract; the wow (field + pencil pass) first, then program lookup and statement, then the validation report.

# PROGRESS: Global Innovation Build Challenge V2

Running log for the unattended cloud build. A resumed session should read this first and continue from **Next up**.

**Deadline:** Thu Oct 1, 2026 · 11:45 AM EDT (`2026-10-01T11:45:00-04:00`)
**All deliverables done by:** Wed Sep 30, 2026 · 11:45 AM EDT (24 h buffer, CLAUDE.md lesson 2)

## Countdown log

| When (ET) | Hours to deadline | Phase |
|---|---|---|
| Wed Sep 23 · 10:35 PM | 181.2 h | 0: setup |

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
| PyTorch | installing from PyPI (download.pytorch.org is blocked) |
| n8n | `N8N_BASE_URL` is **unset**, so there is no API access. Any workflow ships as an importable `n8n/*.json` file |
| Design skills in session | `dataviz`, `ui-demo`, `make-interfaces-feel-better`, `accessibility` loaded. **Missing:** `impeccable`, `emil-design-skills:animate`, taste-skill, `hypersite`. Fallback used: cloned `pbakaus/impeccable`, `emilkowalski/skills`, `leonxlnx/taste-skill` into `/tmp/skills` and read their `SKILL.md` files directly |

### Network policy (important for a resumed session)
The environment is **not** on Full network access. Verified by probing:
- **Allowed:** `github.com` via git, `api.github.com`, `raw.githubusercontent.com`, `media.githubusercontent.com` (LFS), `registry.npmjs.org`, PyPI, `archive.ubuntu.com`, WebSearch.
- **Blocked (403 at the egress proxy):** `devpost.com` and every `*.devpost.com` page (WebFetch too), `huggingface.co`, `download.pytorch.org`, `youtube.com`, `wikipedia.org`, `archive.org`, `unpkg.com`, `cdn.jsdelivr.net`, Yahoo Finance, FRED, SEC, Kaggle, Gutenberg.
- Consequence for research: Devpost pages can't be opened directly. Winner verification uses search-engine results that quote the Devpost page plus the winner's GitHub repo opened through the GitHub API. Each brief states exactly which of those checks passed.
- Consequence for data/models: no Hugging Face downloads. Data must come from GitHub, PyPI/npm packages, or be generated in-repo.

## Log

### Phase 0: setup (Wed Sep 23, 10:35 PM ET · 181.2 h left)
- Read CLAUDE.md, HACKATHON.md, PROMPT.md, hackathon-win SKILL.md + references + templates.
- Checked tools and network (above). Created this file.

## Next up
- Phase 1–2: verify HACKATHON.md facts via search, find 5–8 verified past winners, write `research/`.

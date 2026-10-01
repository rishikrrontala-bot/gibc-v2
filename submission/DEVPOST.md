# Withheld

**Tagline:** College outcomes, with the gaps left in. Explore published earnings, cautious model estimates and the uncertainty behind both.

**Track:** Track 02: Applied (Medical Technology & Finance)

**Team:** Rishik Rontala — solo. Add the existing Devpost account under this real full name; do not create a second account.

## Inspiration

A blank earnings field is not an answer. Students researching college programs encounter missing outcomes without a clear way to distinguish privacy suppression, ordinary missing data and a model's guess. In the June 10, 2026 College Scorecard release, 137,408 of 194,211 program records suppress five-year earnings: 70.8%. Those are program records, not students.

Withheld asks a narrower question than “which college is best?”: can an interface make both the evidence and its uncertainty easier to inspect? The design begins with the gaps rather than concealing them.

## What it does

Withheld is a working, public-data research prototype for exploring college program outcomes. Search 3,568 institutions, filter by field and credential, inspect official earnings or supported estimates, and compare up to three programs. Every estimate carries its source label and a target-80% prediction interval. Programs with fewer than 30 published training peers in the same field and credential receive no estimate. Other types of missing outcomes stay unavailable.

An illustrative fixed-rate loan calculator makes hypothetical monthly payments tangible. A user-controlled comparison benchmark is explicitly not a federal eligibility threshold. CSV exports preserve provenance. The methodology page reports validation, baseline comparisons, small-program performance and limitations.

The app runs without an account, paid inference API or backend. Searches and calculations stay in the browser. This prototype does not automate lending, investments or other real-money decisions.

## How we built it

The interface uses TypeScript, Vite and Canvas 2D, with original typography, layout and motion inspired by Unseen Studio, studied through Mobbin. Instrument Serif, Inter and JetBrains Mono are self-hosted. GitHub Pages serves the static app.

A Python pipeline verifies the official source archives, joins institution attributes and deduplicates pooled program outcomes. Institution families are separated into training, calibration and test groups, with zero OPEID6 overlap. Three LightGBM quantile models use field, broad field, credential, state, institution control and reported completions. Other earnings, debt and institution identifiers are excluded from the predictor set.

Split-conformal corrections expand the initial intervals on a separate calibration group, stratified by completion-size band where enough examples exist. The frozen pipeline exports browser-ready data, model files, split membership and held-out predictions. The browser displays these precomputed outputs; it does not claim to recover suppressed values or run a live LLM.

## Challenges we ran into

The hardest challenge was making missingness and uncertainty honest. Suppressed outcomes have no public ground truth and are not missing at random. A good test result on published programs cannot establish reliability on genuinely suppressed programs.

Pooled branch outcomes also make ordinary random row splits misleading. Grouping by institution family prevents those related records from crossing training and evaluation boundaries. We distinguish program-completion counts from earnings-cohort sizes and keep historical earnings and debt interpretations explicit.

## Accomplishments that we're proud of

The complete journey works: reveal the information gap, search a college, inspect evidence, change a hypothetical loan, compare programs and export labelled results.

On 8,723 held-out published outcomes from 594 institution families, the middle estimate achieves $9,029.87 mean absolute error, compared with $10,247.57 for a field-and-credential training-median baseline. Intervals achieve 77.554% coverage against an 80% target, with mean width $26,179.17. Under-30-completion programs have 74.632% coverage. The shortfall is visible in the interface rather than buried.

Twelve unit/data-integrity tests and three end-to-end browser tests pass, including mobile layout, deep links, exports and retry after a failed data request. An independent script recomputes the evaluation statistics and verifies institution-family separation. Source code, pinned provenance and model artifacts are public.

## What we learned

An uncertainty interval is useful only when people can see where it came from and what it does not mean. A target coverage level is not an observed result, and an observed result is not a guarantee for a different population. Sometimes the most defensible output is no estimate.

## What's next for Withheld

Evaluate another cohort for temporal generalization, investigate the shift between published and suppressed programs, compare stronger baselines and run consent-based usability studies. Future work must validate whether the presentation improves understanding before making claims about decision quality. No user studies or real-world financial impact are claimed in this submission.

## Built with

TypeScript; JavaScript; HTML; CSS; Vite; Canvas 2D; Python; pandas; NumPy; scikit-learn; LightGBM; split-conformal calibration; U.S. Department of Education College Scorecard field-of-study and institution datasets (June 10, 2026 release); Fontsource; Instrument Serif; Inter; JetBrains Mono; Vitest; Playwright; Chromium; GitHub; GitHub Actions; GitHub Pages; OpenAI Codex; Claude Code (Anthropic); Mobbin (design reference research); Impeccable and Emil Kowalski design/animation skill guidance; FFmpeg; Kokoro ONNX (synthetic demo narration); SoundFile. No specialized hardware, commercial LLM inference API or real-money service is required by the app.

## AI-use disclosure

Rishik Rontala directed the project. OpenAI Codex assisted substantially with implementation, the data pipeline, validation, documentation and demo production. Claude Code assisted with earlier concept development and research. The demo uses a disclosed synthetic Kokoro narrator; it does not impersonate Rishik. The app itself uses trained tabular models, not a conversational LLM. No fabricated users, interviews, endorsements or validation results are included.

## Links and media

- Live prototype: https://rishikrrontala-bot.github.io/gibc-v2/
- Public source: https://github.com/rishikrrontala-bot/gibc-v2
- Reproducible evidence: https://github.com/rishikrrontala-bot/gibc-v2/blob/main/docs/MODEL-CARD.md
- Demo video: **Upload `submission/video/demo.mp4` to YouTube (unlisted is acceptable), Vimeo or Youku; paste the resulting watch URL here and into Devpost.**
- Gallery: use `01-the-gap.png`, `03-program-evidence.png`, `04-comparison.png`, `05-validation.png` and `06-limitations.png` from `submission/gallery/`; optional `02-the-model-view.png`.
- Thumbnail: `submission/gallery/thumbnail.png`.

Devpost draft saved: https://devpost.com/software/withheld-uneh3q (project 1455179; submission 1209393). Six gallery screenshots and a thumbnail are uploaded.

This draft is not a submitted competition entry. Review the full name, video URL and selected track before final submission.

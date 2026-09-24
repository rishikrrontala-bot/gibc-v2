# Product

<!-- impeccable:product-schema 1 -->

> Written unattended. Rishik said in his kickoff that he isn't available to answer questions and delegated every decision, so this record is inferred from `CONCEPT.md`, `HACKATHON.md`, `CLAUDE.md` and the research in `research/`. Inferred facts are marked *(inferred)*.

## Platform

web

## Stack

Delegated: Vite + TypeScript static site (CLAUDE.md engineering default), deployed to GitHub Pages at `https://rishikrrontala-bot.github.io/gibc-v2/` with `base: './'`. Python (pandas + scikit-learn/LightGBM) for the offline training pipeline. No backend and no API key: a cold judge visit must never fail.

## Users

- **Primary:** a U.S. high-school junior or senior (and the parent sitting next to them) comparing college programs and the loans that pay for them. They're on a phone or laptop, usually with a specific program in mind: a certificate at a community college, a small bachelor's major, a program at a for-profit school. They're about to sign up for the largest loan of their life so far. *(Persona, not a real user.)*
- **Secondary:** GIBC V2 judges ("industry professionals and academic experts"). They spend minutes per entry, watch the video, maybe open the live link, and score Innovation & Impact, Technical Feasibility, Rigor & Validation, and Presentation.
- **Tertiary** *(inferred)*: school counselors, financial-aid advisers and policy researchers who need program-level numbers the Scorecard doesn't publish.

## Product Purpose

The U.S. Department of Education's College Scorecard publishes what graduates of each program earn and owe, **except when the cohort is small**. Then it prints `PrivacySuppressed`. That happens for 181,758 of 233,979 programs (77.7 %) on median earnings four years after completion. From 2027, a federal earnings test cuts off student loans to programs whose graduates earn less than a typical high-school graduate. Withheld estimates the withheld numbers from patterns in the published ones, with calibrated uncertainty, so a family can see which side of that line a program likely falls on before they borrow.

Success = a student searches a program, understands in one glance whether the number is **published or estimated**, where it sits against their state's line, what the loan payment would be, and how sure the estimate is. A judge sees a validated model, not a guess.

## Positioning

Every other college-ROI tool (the Scorecard itself, CollegeTrue, FREOPP's ROI study, Georgetown CEW) either shows only the published programs or fills gaps with generic, unlabelled averages. Withheld is the only one that (1) estimates suppressed programs individually, (2) attaches **split-conformal 80 % intervals calibrated by program size**, validated on held-out real programs, and (3) states plainly what it will not do: reverse-engineer private data.

## Operating Context

- Used in the middle of a college decision, often on a phone, often with a parent. Moments of anxiety about money.
- Judges view it on a laptop, often muted, often after watching the 2–5 minute video.
- The data refreshes a few times a year (College Scorecard releases); the pipeline is re-runnable.

## Capabilities and Constraints

- Search all 233,979 programs (institution × 4-digit CIP field × credential level).
- Official figure when published; model estimate + 80 % interval when suppressed. Never mix the two without a label.
- Compare against the federal earnings threshold for the program's state and credential level.
- Debt → standard 10-year payment → debt-to-earnings ratio.
- A validation page: accuracy vs. baselines, interval coverage by size band and credential, error analysis.
- **Constraint:** static site; all data shipped as compressed files; first load under 2.5 s on 4G (so the full field loads progressively).
- **Constraint:** it isn't the official Department of Education determination and isn't financial advice. Say so where a verdict appears.
- **Open:** the per-state high-school earnings thresholds need a verifiable source. If none is reachable, use the Scorecard's own `EARN_GT_THRESHOLD` fields and document it.

## Brand Commitments

- Name: **Withheld**.
- Visible credit "Built by Rishik Rontala" and `<meta name="author" content="Rishik Rontala">`.
- Voice: plain, exact, a little dry. Numbers carry their units and their uncertainty. No hype, no fear-mongering, no emoji.
- The art direction must be this entry's own (Rishik is running 15 entries at once; no shared template). Banned by CLAUDE.md: purple/blue gradients, centered-card SaaS templates, emoji section headers, Playfair + drop shadows, generic 3D blobs, stock hero illustrations.

## Evidence on Hand

- `College Scorecard Most-Recent-Cohorts-Field-of-Study` (233,979 rows × 160 columns) and `…-Institution` files, public domain, via the Amherst-Statistics/CollegeScorecard mirror (updated Mar 18 2026). Hashes are recorded in the pipeline.
- Published policy facts, each with a source URL (research/RESEARCH-BRIEF.md): OBBBA earnings test; the STATS / Earnings Accountability final rule of Jul 1 2026; the benchmark definition (median earnings of HS-diploma holders aged 25–34).
- **Absent, and must not be fabricated:** user testimonials, usage numbers, partnerships, endorsements, interviews. The model's accuracy numbers only ever come from `pipeline/` output files.

## Product Principles

1. **Published and estimated never look the same.** The visual system encodes provenance before it encodes value.
2. **Uncertainty is the product, not a disclaimer.** An interval that's honest about being wide beats a point estimate that looks sure.
3. **One verdict, then the evidence.** Plain words first ("likely below the line"), numbers one step down, methodology one step further.
4. **Refuse the privacy shortcut.** Never back out suppressed values; say so.
5. **Every number is reproducible** from `pipeline/` in this repo.

## Accessibility & Inclusion

WCAG 2.2 AA. Every chart has a text equivalent (the program card states its numbers in words). Colour is never the only encoding of above / below / uncertain. Keyboard search and navigation. `prefers-reduced-motion` respected, especially in the field animation. Works at 375 px.

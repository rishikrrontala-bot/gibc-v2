# Withheld — ML Empowerment Build Challenge 3.0

Prepared October 2, 2026. This is a proposed alternate entry, not proof of submission.

Event: https://ml-build-challenge-3.devpost.com/
Project: https://devpost.com/software/withheld-uneh3q
Live app: https://rishikrrontala-bot.github.io/gibc-v2/
Source: https://github.com/rishikrrontala-bot/gibc-v2

## Live requirements review

- User is already registered. Submission phase is open.
- Current configured deadline: 2026-10-10T06:45:00Z — October 10, 2026 at 2:45 AM EDT. Older rules prose still says October 5 at 9 PM PDT; the live configured date is later. Submit promptly instead of relying on that discrepancy.
- Rules: “Open to students high school and college level.” “Solo submissions are allowed.”
- No required custom questions. Hosted video, website and ZIP are not mandatory.
- At least one file showing functionality or design is required. Six screenshots and a thumbnail are already attached to the project.
- Name, tagline, technical description, AI-use disclosure, target users, sole participant, public repository, working app and validation evidence are prepared.
- Local credential scan: no high-confidence secret patterns, generic credential assignments or credential files found.
- GIBC remains an unsubmitted draft. YouTube upload did not complete; this does not prevent the proposed ML entry because a hosted video is optional.

## Exact proposed project write-up

## Entry context and intended users

Withheld is proposed for ML Empowerment Build Challenge 3.0 as an AI/data-science research prototype. Target users are students and families researching college programs, and school counselors helping them interpret incomplete outcome data. Rishik Rontala is the sole participant, directing the design, implementation, model evaluation and submission with disclosed AI coding assistance.

Prior-work disclosure: this project began with concept research and planning for Global Innovation Build Challenge V2 in September 2026. The working interface, current-data training pipeline, validation, deployment and demo were completed on October 1, 2026. The GIBC entry remained a draft when that event closed; it was not submitted. The same project and history are being disclosed here. The model is a tabular quantile-boosting system, not a foundational LLM.

Inspiration

A blank earnings field is not an answer. Students researching college programs encounter missing outcomes without a clear way to distinguish privacy suppression, ordinary missing data and a model's guess. In the June 10, 2026 College Scorecard release, 137,408 of 194,211 program records suppress five-year earnings: 70.8%. Those are program records, not students.

Withheld asks a narrower question than “which college is best?”: can an interface make both the evidence and its uncertainty easier to inspect? The design begins with the gaps rather than concealing them.

What it does

Withheld is a working, public-data research prototype for exploring college program outcomes. Search 3,568 institutions, filter by field and credential, inspect official earnings or supported estimates, and compare up to three programs. Every estimate carries its source label and a target-80% prediction interval. Programs with fewer than 30 published training peers in the same field and credential receive no estimate. Other types of missing outcomes stay unavailable.

An illustrative fixed-rate loan calculator makes hypothetical monthly payments tangible. A user-controlled comparison benchmark is explicitly not a federal eligibility threshold. CSV exports preserve provenance. The methodology page reports validation, baseline comparisons, small-program performance and limitations.

The app runs without an account, paid inference API or backend. Searches and calculations stay in the browser. This prototype does not automate lending, investments or other real-money decisions.

How we built it

The interface uses TypeScript, Vite and Canvas 2D, with original typography, layout and motion inspired by Unseen Studio, studied through Mobbin. Instrument Serif, Inter and JetBrains Mono are self-hosted. GitHub Pages serves the static app.

A Python pipeline verifies the official source archives, joins institution attributes and deduplicates pooled program outcomes. Institution families are separated into training, calibration and test groups, with zero OPEID6 overlap. Three LightGBM quantile models use field, broad field, credential, state, institution control and reported completions. Other earnings, debt and institution identifiers are excluded from the predictor set.

Split-conformal corrections expand the initial intervals on a separate calibration group, stratified by completion-size band where enough examples exist. The frozen pipeline exports browser-ready data, model files, split membership and held-out predictions. The browser displays these precomputed outputs; it does not claim to recover suppressed values or run a live LLM.

Challenges we ran into

The hardest challenge was making missingness and uncertainty honest. Suppressed outcomes have no public ground truth and are not missing at random. A good test result on published programs cannot establish reliability on genuinely suppressed programs.

Pooled branch outcomes also make ordinary random row splits misleading. Grouping by institution family prevents those related records from crossing training and evaluation boundaries. We distinguish program-completion counts from earnings-cohort sizes and keep historical earnings and debt interpretations explicit.

Accomplishments that we're proud of

The complete journey works: reveal the information gap, search a college, inspect evidence, change a hypothetical loan, compare programs and export labelled results.

On 8,723 held-out published outcomes from 594 institution families, the middle estimate achieves $9,029.87 mean absolute error, compared with $10,247.57 for a field-and-credential training-median baseline. Intervals achieve 77.554% coverage against an 80% target, with mean width $26,179.17. Under-30-completion programs have 74.632% coverage. The shortfall is visible in the interface rather than buried.

Twelve unit/data-integrity tests and three end-to-end browser tests pass, including mobile layout, deep links, exports and retry after a failed data request. An independent script recomputes the evaluation statistics and verifies institution-family separation. Source code, pinned provenance and model artifacts are public.

What we learned

An uncertainty interval is useful only when people can see where it came from and what it does not mean. A target coverage level is not an observed result, and an observed result is not a guarantee for a different population. Sometimes the most defensible output is no estimate.

What's next for Withheld

Evaluate another cohort for temporal generalization, investigate the shift between published and suppressed programs, compare stronger baselines and run consent-based usability studies. Future work must validate whether the presentation improves understanding before making claims about decision quality. No user studies or real-world financial impact are claimed in this submission.

Built with

TypeScript; JavaScript; HTML; CSS; Vite; Canvas 2D; Python; pandas; NumPy; scikit-learn; LightGBM; split-conformal calibration; U.S. Department of Education College Scorecard field-of-study and institution datasets (June 10, 2026 release); Fontsource; Instrument Serif; Inter; JetBrains Mono; Vitest; Playwright; Chromium; GitHub; GitHub Actions; GitHub Pages; OpenAI Codex; Claude Code (Anthropic); Mobbin (design reference research); Impeccable and Emil Kowalski design/animation skill guidance; FFmpeg; Kokoro ONNX (synthetic demo narration); SoundFile. No specialized hardware, commercial LLM inference API or real-money service is required by the app.

AI-use disclosure

Rishik Rontala directed the project. OpenAI Codex assisted substantially with implementation, the data pipeline, validation, documentation and demo production. Claude Code assisted with earlier concept development and research. The demo uses a disclosed synthetic Kokoro narrator; it does not impersonate Rishik. The app itself uses trained tabular models, not a conversational LLM. No fabricated users, interviews, endorsements or validation results are included.


## Pending action

Confirm final submission to ML Empowerment Build Challenge 3.0. On confirmation, update the project with the context above, submit the existing Withheld project (1455179), and verify submitted_at live. Do not claim completion from this document alone.

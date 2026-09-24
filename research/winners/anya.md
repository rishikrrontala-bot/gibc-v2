# Winner brief: Anya

**Hackathon:** Iris Hacks IV, 2026 (a 2-day student AI hackathon) · **Prize won:** 1st Place Overall, "$300 in Featherless credits + $250 cash prize", per HackWinnerDB entry `anya-9jsrhq`
**Submission URL:** https://devpost.com/software/anya-9jsrhq · **Repo:** https://github.com/Dishank-Sen/Anya · **Demo video:** not viewable from this network
**Verified:** page loaded ☐ (blocked) · prize stated ☑ (HackWinnerDB) · video played ☐ · repo opened ☑

**Why it's in this set:** the **same sponsor and the same prize** as GIBC V2's Grand Champion award ($300 Featherless AI credits for the overall best project).

## Pitch, verbatim
> India produces enough food to feed its entire population. Yet **35.5% of children under 5 are stunted** and **57% of women are anemic.** We don't have a food crisis. We have a **nutrition intelligence failure.**

## The wow moment
A district heat-map of India. Clicking Alirajpur shows "Iron: 79% CRITICAL" with a per-micronutrient breakdown, then a fortification plan and a 7-day culturally specific meal plan costed at "₹847 per person".

## Demo teardown
- Length / first 15 s: not viewable.
- Real data: **partially.** District figures come from NFHS-5 factsheets, stored as a hand-built JSON of the top 10 districts.

## Scope reality (the important part)
- The README's "How we built it" table claims "XGBoost + LSTM (PyTorch)", PostgreSQL and Redis.
- The code says otherwise: `backend/services/risk_predictor.py` opens with *"No ML needed — data is already sourced from verified NFHS-5 (2019-21) district factsheets."* The "XGBoost + LSTM Ensemble Prediction" label is a string literal in `main.py`. There's no training code, and the backend totals 944 lines.
- Commit window: 2 commits, both on Aug 9 2026.
- **Lesson:** at student events, judges score the pitch, the specific statistic and the demo; they don't audit the code. The claims-vs-code gap wasn't penalised *here*. We still won't do this (CLAUDE.md, never fabricate). The upside is that a *real* validated model, shown clearly, is a genuine differentiator.

## Stack
React, D3, Mapbox, FastAPI, an LLM for meal text, PuLP for linear programming.

## Submission page shape
Long-form Devpost sections (Inspiration → What it does → How we built it → Challenges → What we learned → What's next), each dense with specific numbers, tables and named datasets.

## Why this won (one sentence)
A staggering, specific, sourced statistic in the first sentence, an ambitious three-stage story (Predict → Fortify → Nourish) and a map you can click.

## Transferable to us
- **Copy:** open with a hard, sourced number, and name the government datasets. Structure the story as a pipeline with named stages.
- **Copy:** specificity (one named place, one named number) beats generality.
- **Beat it on:** every claim backed by code and a reproducible number. Say so explicitly ("every figure on this page is recomputed by `npm run verify`").

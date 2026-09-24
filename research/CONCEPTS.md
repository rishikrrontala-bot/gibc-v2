# Concepts: three scored, one picked

Decided Wed Sep 23 2026, 10:56 PM ET (180.8 h to deadline). Rishik delegated the pick (CLAUDE.md override), so the highest weighted score wins.

## Scoring method
The tracks have different official rubrics with unpublished weights, so each concept is scored 1–5 on **its own track's criteria, equally weighted** (the event's stated criteria), and that average carries 60 %. Two cross-cutting factors decide *placing* rather than quality, so they carry the other 40 %:
- **Field (20 %):** how beatable the visible competition in that track is (`FIELD-SCAN.md`).
- **Feasibility here (20 %):** can this VM (4 vCPU, no GPU, Hugging Face / Devpost / most data hosts blocked) produce it properly in the 6-day window, with real data.

## The three concepts

### A. Four Cores (Track 01, TECH)
**Pitch:** a from-scratch ~15M-parameter language model trained entirely on 4 CPU cores, with the whole training run replayable and the model running in the browser.
**Wow moment:** type a prompt and watch a model that was trained on a laptop-class CPU generate text in the page, with the loss curve beside it.
**Riskiest unknown:** training data. FineWeb, TinyStories and WikiText all live on Hugging Face, which is blocked. **Cut first:** reasoning probes.

| Track 01 criterion | Score | Why |
|---|---|---|
| Perplexity & accuracy | 1 | Against five GPU entries (best: WikiText-103 PPL 31.8 at 7.2 B tokens), a CPU run of ~0.3 B tokens can't compete |
| Reasoning performance | 1 | HellaSwag/ARC at this scale sit at chance |
| Training efficiency | 4 | The CPU-only story is real and measurable (FLOPs, tokens/s, wall clock) |
| Innovation | 2 | Vocabulary budget (×2), data filtering, rigour and in-browser inference are all already taken |
| Documentation & demo | 4 | In-browser inference is a good demo |
| **Track average** | **2.4** | |
| Field | 1 | ≥ 5 GPU-trained 49M entries |
| Feasibility here | 2 | No GPU, no Hugging Face corpora or eval sets |
| **Weighted** | **2.04** | 0.6×2.4 + 0.2×1 + 0.2×2 |

### B. Withheld (Track 02, Applied: Finance) ← **picked**
**Pitch:** *The federal College Scorecard withholds the earnings figure for 3 in 4 U.S. college programs. Withheld estimates it, with calibrated uncertainty, and shows which side of the new federal earnings line each program likely falls on, before a student borrows for it.*
**Wow moment:** a field of all 233,979 programs, three-quarters of them grey ("PrivacySuppressed"). The model resolves the grey into estimates with uncertainty bars, the state earnings line sweeps across, and a searched program lands as "likely below the line", with the loan payment that implies.
**Riskiest unknown:** covariate shift. Suppressed programs are *small*, and the model learns from larger ones. Mitigation: validate on the smallest published programs, calibrate intervals by size band (Mondrian split-conformal), and state the untestable assumption plainly. **Cut first:** repayment-status (default/delinquency) modelling, keeping earnings + debt.

| Track 02 criterion | Score | Why |
|---|---|---|
| Innovation & impact | 5 | Nobody publishes calibrated estimates for suppressed programs; the July 2026 federal rule makes the earnings line consequential (loss of loan eligibility); the user is a student about to take the largest loan of their life |
| Technical feasibility | 5 | Data is in hand (233,979 rows, public domain, mirrored on GitHub); gradient-boosted quantile models train in minutes on CPU; runs as a static site |
| Rigor & validation | 5 | Institution-grouped held-out validation, three baselines, conformal coverage checked per size band and credential, a reproducible pipeline with hashes. This is where the field and past winners are weakest |
| Presentation | 4 | Strong visual; the risk is overloading a judge with statistics. Solve it with a single verdict per program |
| **Track average** | **4.75** | |
| Field | 4 | Two visible finance entries, neither consumer-facing nor validated |
| Feasibility here | 5 | Everything runs on this VM; no key, no backend |
| **Weighted** | **4.65** | 0.6×4.75 + 0.2×4 + 0.2×5 |

### C. Second Ask (Track 02, Applied: Finance)
**Pitch:** when an algorithm denies your credit application, get the specific reasons and the *smallest actionable change* that would flip it (algorithmic recourse, per Ustun et al. 2019), with immutable traits like age never suggested.
**Wow moment:** a denial, then a "cheapest path to yes" plan, then fast-forward and the decision flips.
**Riskiest unknown:** data. HMDA (ffiec.cfpb.gov) and FICO HELOC are unreachable or unclearly licensed; the reachable fallback is UCI German Credit (1,000 rows, Germany 1994). **Cut first:** fairness analysis.

| Track 02 criterion | Score | Why |
|---|---|---|
| Innovation & impact | 4 | Real research area with a CFPB hook (specific adverse-action reasons for complex models) |
| Technical feasibility | 4 | Linear recourse is solvable exactly in the browser |
| Rigor & validation | 3 | 1,000 rows from 1994 limits every claim |
| Presentation | 4 | The flip is a good beat |
| **Track average** | **3.75** | |
| Field | 3 | Credit-fairness demos are common (FairLend won with one this year) |
| Feasibility here | 3 | The good datasets are blocked |
| **Weighted** | **3.45** | |

## Result

| | A. Four Cores | **B. Withheld** | C. Second Ask |
|---|---|---|---|
| Track | 01 TECH | **02 Applied: Finance** | 02 Applied: Finance |
| Track rubric avg (60 %) | 2.4 | **4.75** | 3.75 |
| Field (20 %) | 1 | **4** | 3 |
| Feasibility here (20 %) | 2 | **5** | 3 |
| **Weighted** | 2.04 | **4.65** | 3.45 |

**Pick: B, Withheld.** It wins on every column. It also fits Rishik's lane rules: HACKATHON.md said "prefer Finance: UnivaBio and DSH already cover health". It doesn't overlap any sibling claimed so far (Low Sun, for Practice to Create, is the only one claimed at pick time) or any past project. LeaseLeak (rent rolls vs HUD/Zillow) is housing, not student credit. Explain It Back is study, not money.

**Track 03 (Open)** wasn't scored as a column. Its rubric (creativity, execution, impact, presentation) has no rigour criterion, which is where this entry's advantage lies. Open tracks draw the most entries, and eight of Rishik's fifteen sibling events are open-lane, which makes overlap likely.

## Pre-mortem: "it's Oct 8 and Withheld didn't place. Why?"
1. *Judges read it as education, not finance.* → Lead with the loan: debt, payment, loan-eligibility loss, repayment outcomes. Name the metric the rule uses (the earnings test) and the finance metric (debt-to-earnings).
2. *Too many statistics.* → One verdict per program in plain words; the stats sit one click down.
3. *"You're un-suppressing private data."* → Say plainly, early, that we never reverse suppressed values. The model learns from other programs; intervals are wide where they should be. Put it in LIMITATIONS and in the video.
4. *No wow in the first 15 s.* → The fog-lifting field opens the video.
5. *It broke live.* → A static site with pre-computed estimates plus an in-browser model, both tested in Playwright on the live URL.

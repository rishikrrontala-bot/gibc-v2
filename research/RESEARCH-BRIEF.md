# Research brief: GIBC V2

Compiled Wed Sep 23 2026, 10:35–10:56 PM ET. Sources: web search (Devpost pages are blocked from this VM, so the event facts come from the search index's copy of `gibc-v2.devpost.com`), six winner briefs (`winners/`), and a scan of the live GIBC V2 field (`FIELD-SCAN.md`).

## 1. Event facts, re-verified

| Fact | Status |
|---|---|
| Deadline **Oct 1, 2026, 11:45 PM GMT+8 = 11:45 AM EDT** | ✅ confirmed (search index of the event page: "before the October 1, 11:45pm GMT+8 deadline") |
| Build period Jul 11 – Oct 1 2026; teams of 1–6; one track per project; closing ceremony Oct 8 | ✅ confirmed |
| Students only, 13+ | ✅ per HACKATHON.md, consistent with the "student-led" framing |
| Six required components: description, public repo **with README (setup, prerequisites, usage) so judges can run it**, **2–5 min video (YouTube/Vimeo/Youku), English audio or English subtitles**, complete Built With, team members by real full name, **≥ 3 high-quality images** | ✅ confirmed |
| Submission form also asks for **hosted demo URL** and **testing instructions** | ✅ new; added to HACKATHON.md |
| Track 02: "empirical, real-world data science, predictive ML, or automated financial or medical pipelines"; **datasets must be public or de-identified** | ✅ new detail; added |
| Track 02 judging: Innovation & Impact · Technical Feasibility · **Rigor & Validation** ("quality of research, experimental design, data collection, and validation") · Presentation ("clarity of demo and communication") | ✅ confirmed; weights still unpublished → treated as equal |
| All tracks, per the event page: strong submissions show "a working prototype, a complete end-to-end flow, handling of real-world complexity, and documentation clear enough that another developer could understand, run, and build on top of your work" | ✅ new; this is effectively a fifth, cross-cutting criterion |
| Track 01 cap "includes token embeddings and the output head" | ✅ confirmed (quoted by two entrants) |
| Grand Champion: "Featherless AI Grand Award", $300 Featherless credits, the **overall highest-scoring project across the three tracks** | ✅ confirmed |
| Judges: "a panel of industry professionals and academic experts" (international) | ✅ names not in the index |

## 2. Problem shape that wins (at events like this)
**Specific, sourced, felt.** Every winner opens with a concrete, checkable claim about real people: Anya ("35.5 % of children under 5 are stunted"), CollegeTrue ("your real monthly loan payment as a % of your first paycheck"), FairLend ("Same income. Same credit score. Different zip code."). Two of six are household-finance problems a student can personally feel. None is a general platform.

## 3. Demo shape that wins
**One clickable, zero-setup moment that makes an abstract risk concrete.** GridSense's floor plan (click the fan, *hear* it failing), DebtShield's checkout overlay (this purchase drops your solvency odds), FairLend's two identical applicants with different outcomes. Judges can reach each one without an account or an API key (FairLend is the exception, and it's the weakest demo of the six).

## 4. Scope ceiling
Weekend-to-week builds: one core model plus one strong interactive surface plus a long-form writeup. The long 10-week window for GIBC doesn't raise the bar on features; the visible GIBC field raises it on **evidence** (AryaErgin's hashes, protocols and negative results).

## 5. What winners skipped
- **Validation.** Anya's claimed ML doesn't exist in the code; GridSense validated on synthetic audio; CollegeTrue uses 10 hardcoded salaries. None reports calibration or uncertainty.
- Tests, CI and accessibility: absent in all six.
- **So:** rigour is where judges' expectations are low and GIBC Track 02 explicitly scores it. That's the gap to own. Tests and CI still don't score directly, so they stay cheap.

## 6. Judge bias
"Industry professionals and academic experts", with a sponsor (Featherless AI) that sells LLM inference. The academic half will reward correct methodology (held-out validation, calibrated intervals, honest limitations). The industry half will reward a clear product and a real user. The sponsor's interest is LLMs, but the Grand Champion is scored on overall merit, not sponsor use. **Don't bolt on an LLM for the sponsor's sake.**

## 7. The decision the research forces
The hypothesis in HACKATHON.md was "TECH or Applied-Finance". The field scan overturns TECH: at least five GPU-trained ~49M-parameter entries already exist, one at WikiText-103 PPL 31.8 on 7.2 B tokens. This VM is CPU-only, and Hugging Face (the source of every standard pretraining corpus and eval set) is blocked. **Applied-Finance** has two visible finance entries (actuarial fire risk and DeFi scams), no consumer-finance entry, and an explicit rigour criterion.

**Data that is reachable from this network and fits Track 02:** the U.S. Department of Education **College Scorecard**, program-level ("Field of Study") and institution-level files, mirrored in the public [Amherst-Statistics/CollegeScorecard](https://github.com/Amherst-Statistics/CollegeScorecard) R-package repo (last updated Mar 18 2026). Profiled:
- **233,979** program rows (institution × 4-digit CIP × credential), 160 columns: median debt, median earnings 1 and 4 years after completion, loan repayment status 1–4 years into repayment (default, delinquency, forbearance, making progress…), and the share earning more than a typical high-school graduate.
- **Only 52,221 programs (22.3 %) publish a median earnings figure 4 years out; 181,758 (77.7 %) are `PrivacySuppressed`.** Median debt is published for 48,143 (20.6 %).
- Counterweight, which must appear alongside it: suppressed programs are small, so by *graduates* the gap is much smaller (one analysis found 14 % of federally aided bachelor's recipients in suppressed programs). Both numbers go in the pitch.

**Policy hook (verified via search):** the One Big Beautiful Bill Act's "do no harm" earnings test. ED's STATS / Earnings Accountability final rule was issued **July 1, 2026**, most provisions effective July 1, 2027, with the first test applied to the 2027–28 award year. A program whose median graduate earns less than a typical high-school graduate aged 25–34 (the undergraduate benchmark; state thresholds range from about $26.5k in Mississippi to $36.6k in New Hampshire) in two of three years **loses federal student-loan eligibility**. An analysis of the 41,414 associate's and bachelor's programs *with* reported earnings found 5,943 (14.3 %) failing outright, and short certificates fail about 29 % of the time. For the ~78 % of programs with no public earnings figure, families can't see which side of the line a program is on.

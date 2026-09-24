# Winner brief: FairLend

**Hackathon:** Scarlet Hacks, 2026 · **Prize won:** Best FinTech Project, per HackWinnerDB entry `fairlend-cj805r`
**Submission URL:** https://devpost.com/software/fairlend-cj805r · **Repo:** https://github.com/Sashank006/FairLend · **Demo video:** not viewable from this network
**Verified:** page loaded ☐ (blocked; the search index didn't surface it either) · prize stated ☑ (HackWinnerDB) · video played ☐ · repo opened ☑

## Pitch, verbatim
> Same income. Same credit score. Different zip code. Different answer. FairLend finds out why.  *(Devpost tagline, via HackWinnerDB)*

README: "An AI bias auditor for mortgage lending models, built on real HMDA data."

## The wow moment
The **Applicant Simulator**: two synthetic applicants ("Maria" and "James") with identical loan amount, income, DTI and property value but different race and sex go through the live model, and the confidence gap appears side by side.

## Demo teardown
- Length / first 15 s: not viewable.
- Real data: **yes.** About 228,000 Illinois HMDA applications (CFPB). The CSV isn't committed (too large), and the README gives download steps.
- The LLM (Groq, llama-3.3-70b) drafts a "compliance-style risk report" from the computed metrics.

## Scope reality
- Working per the code: XGBoost approval model (GridSearchCV), fairlearn demographic-parity and equalized-odds gaps, feature importances, the two-applicant demo, an LLM memo, and a three-tab React dashboard.
- Honest scoping line in the README: "a demonstration of what a fair-lending audit pipeline … could look like, not a production risk tool."
- Commit window: 3 commits (Apr 4 → Aug 19 2026). Most of the work landed in a single commit.

## Stack
Python, pandas, scikit-learn, XGBoost, SHAP, fairlearn, FastAPI, Groq, React + Vite + recharts. Needs a backend and an API key, so a judge can't just click a link.

## Submission page shape
Tagline is four short sentences with a rhythm ("Same X. Same Y. Different Z."). Leads with the unfairness, not the tech.

## Why this won (one sentence)
Real regulator data plus a single side-by-side comparison that makes an abstract fairness metric visceral.

## Transferable to us
- **Copy:** a real federal dataset, cited, as the credibility anchor; a regulatory hook (ECOA / Fair Housing → for us, the 2026 earnings-accountability rule); a two-item comparison as the emotional beat.
- **Copy:** the scoping sentence ("not a production tool"). Documented restraint.
- **Beat it on:** judge access (static site, no key, no backend) and validation (they report fairness gaps but no calibration or held-out uncertainty).

# Winner brief: GridSense

**Hackathon:** Global Tech Innovation Challenge, 2026 ("An international student hackathon innovating software and electrical engineering solutions for real-world impact") · **Prize won:** Grand Prize Champion Certificate, per HackWinnerDB entry `gridsense-cjuofz`
**Submission URL:** https://devpost.com/software/gridsense-cjuofz · **Repo:** https://github.com/mvkpsai-gif/gridsense (a copy also exists at `sahishnu-m/gridsense`) · **Demo video:** not viewable
**Verified:** page loaded ☐ (blocked; the search index confirms the event page and the project's GitHub) · prize stated ☑ (HackWinnerDB) · video played ☐ · repo opened ☑

**Why it's in this set:** the closest event shape to GIBC (international, online, student-run Devpost event with a single "innovation" judging lens), and a **Grand Prize**.

## Pitch, verbatim (from `SUBMISSION.md`)
> Hear failure before it happens: acoustic predictive maintenance from any microphone, 100% offline.
> Industrial machines fail loudly long before they fail catastrophically: a bearing whines, a rotor wobbles, a fan grinds.

## The wow moment
`demo.html`: a landing page scrolls into a **top-down floor plan of a house with seven running appliances**. Click one and you *hear* it (synthesised live with Web Audio) and see the diagnosis computed live by an in-page FFT. Two appliances are failing, three show early warnings, two are healthy.

## Demo teardown
- Length / first 15 s: not viewable; `DEMO_SCRIPT.md` exists in the repo.
- Data: **synthetic.** A "physics-based synthetic-audio generator" makes 240 clips (3 classes). They reported 98.3 % held-out accuracy on it.
- Judging criterion in their own submission copy: "Overall Innovation (creativity, execution, impact) · peer-voted."

## Scope reality
- Working: synthetic data generator, features (MFCC, spectral centroid/rolloff, ZCR, RMS), RandomForest, Streamlit dashboard, a standalone interactive HTML demo, a pitch deck and a one-pager.
- Honest note they *led* with: "its single misclassification is a *mild* friction case read as healthy, surfacing the genuine hard problem of early fault detection."
- Commit window: 4 commits (Jul 23 → Sep 17 2026).

## Stack
Python, Librosa/SciPy, scikit-learn, Streamlit, plus a zero-dependency `demo.html`. "100 % offline, no API keys" was part of the pitch.

## Submission page shape
Tagline → a "real-world problem" field → What it does (4 verbs: Listens / Analyses / Diagnoses / Advises) → How we built it → What makes it innovative (4 bullets) → Impact.

## Why this won (one sentence)
A self-contained, clickable, sensory demo (you hear the broken fan) that runs with no setup, plus one honest limitation stated up front.

## Transferable to us
- **Copy:** a zero-setup interactive demo that judges can click (static site, no keys), and the "no API keys, runs locally, your data never leaves" line.
- **Copy:** leading with the honest failure case. Our version: "here's where the model is least sure, and why".
- **Copy:** the four-verb "What it does" list.
- **Beat it on:** real federal data instead of synthetic clips; validation on held-out real programs.

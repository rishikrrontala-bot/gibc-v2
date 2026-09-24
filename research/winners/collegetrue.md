# Winner brief: CollegeTrue

**Hackathon:** West Hacks, 2026 ("Create a fintech app to help educate people") · **Prize won:** 2nd place (plus "Charity Donation: 1st, 2nd & 3rd Place"), per HackWinnerDB entry `collegetrue-west-hacks`
**Submission URL:** https://devpost.com/software/collegetrue · **Repo:** https://github.com/Bear876/collegetrue · **Live:** https://bear876.github.io/collegetrue/ · **Demo video:** not viewable from this network
**Verified:** page loaded ☐ (devpost.com blocked; page text confirmed through the search index) · prize stated ☑ (HackWinnerDB, imported from Devpost) · video played ☐ (YouTube blocked) · repo opened ☑

## Pitch, verbatim
> See what college really costs before it's too late. Enter 3 schools, get your real monthly loan payment as a % of your first paycheck. No sugarcoating.

The README opens: "CollegeTrue is a web app that gives US high‑school students a financial reality check on their college options by comparing loan burden as a percent of their first paycheck."

## The wow moment
Three schools go in, and "one brutally honest call" comes out: the monthly payment shown as a share of your first paycheck, with burden bars and an age-25 budget snapshot. The verdict framing is the hook.

## Demo teardown
- Length / first 15 s: not viewable (YouTube blocked).
- The live site's first screen (from `index.html`): serif headline "Pick a college with your *future paycheck*", a stat row, and one CTA ("Run my reality check"). The value proposition fits in one line.
- Real data or hardcoded: **mixed.** It calls the College Scorecard API with the public `DEMO_KEY` and falls back to a hardcoded `SCHOOLS` table. Salaries come from a hardcoded table of 10 majors (`MAJOR_SALARIES`, e.g. CS $88k, Education $41k).

## Scope reality
- Working: school lookup (API or fuzzy local match), 4-year cost, 10-year payment, % of take-home, timeline.
- Stated assumption #1 in the README: "Salaries are agnostic of which college you attend." Program-level variation, the thing the federal data actually measures, is ignored.
- Commit window: 36 commits, May 31 → Jun 1 2026 (about 16 h, a weekend build).

## Stack
Vanilla HTML/CSS/JS, College Scorecard API, GitHub Pages. The stack isn't the story; the verdict is.

## Submission page shape
From the search index: leads with the one-line pitch, then "brutally honest, easy-to-use", then the Scorecard API integration and the financial model (4-year cost → 10-year payment → burden as % of starting salary).

## Why this won (one sentence)
A problem every high-school senior feels, reduced to one honest number (payment ÷ paycheck), shipped as a clean one-screen tool in a weekend.

## Transferable to us
- **Copy:** the framing. One personal, felt number, and a verdict in plain words. The high-schooler persona is Rishik's own.
- **Copy:** the Scorecard as the data spine. Judges at a *fintech* event accepted college debt as finance.
- **Beat it on:** program-level data instead of 10 hardcoded majors; the 78 % of programs whose earnings the Scorecard suppresses (CollegeTrue silently falls back to generic estimates there); validated uncertainty instead of "illustrative" numbers.
- **Don't copy:** a fallback to made-up numbers that looks the same as real data.

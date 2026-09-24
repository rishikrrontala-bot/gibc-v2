# Winner briefs: how these were found and verified

**Why no GIBC V1 winners.** GIBC V1 (`global-innovation-challenge-v1.devpost.com`) is the only prior edition. Its winners are listed only on the Devpost gallery. This cloud session's network policy blocks every `devpost.com` host (HTTP 403 at the egress proxy, for WebFetch and curl alike). Five web searches for V1 winners (`site:devpost.com`, "winner", "1st Place Overall", organizer Instagram, LinkedIn) returned the V1 overview, rules and updates pages but no project names. So no V1 winner is cited here, because none could be verified.

**Where these came from.** [HackWinnerDB](https://github.com/notsointresting/hackwinnerdb) (MIT code, CC BY 4.0 data) is an open database of 4,174 winning entries with the award text and Devpost URL imported from Devpost's winner flags. I cloned it (commit on `main`, Sept 2026) and filtered for, in the skill's priority order:

1. Same organizer: not identifiable (GIBC is run by an unnamed student team).
2. **Same sponsor:** Featherless AI funds GIBC V2's Grand Champion prize ($300 in credits). Anya won an identical prize.
3. **Similar event shape:** GridSense and AccessLens won grand prizes at other international, online, student-run Devpost events.
4. **Same domain (Applied: Finance):** CollegeTrue, FairLend, DebtShield.

**Verification bar, as met.** For each brief:
- ☑ Award text taken from the HackWinnerDB entry, which records the Devpost submission URL. Where the repo's own README states the award, that's noted too.
- ☑ Devpost page content cross-checked through the search engine's index where it surfaced (noted per brief).
- ☑ **Repo opened**: cloned from GitHub, README and source read, commit window measured with `git log`.
- ☐ Devpost page loaded directly: **not possible from this network** (403).
- ☐ Demo video watched: **not possible** (`youtube.com` blocked). Video facts come from repo files only, and are marked as such.

All six are from 2026, inside the 24-month window.

| Brief | Event (2026) | Award | Why it's here |
|---|---|---|---|
| [collegetrue.md](collegetrue.md) | West Hacks | 2nd place | Same domain: college cost vs. first paycheck, built on College Scorecard |
| [fairlend.md](fairlend.md) | Scarlet Hacks | Best FinTech Project | Same track shape: real public finance data → model → audit |
| [debtshield.md](debtshield.md) | Warwick Finance Societies Fintech Hackathon | Best Overall Hack + Best Financial Inclusion | Finance: probabilistic risk made legible |
| [anya.md](anya.md) | Iris Hacks IV | 1st Place Overall ($300 Featherless credits + $250) | Same sponsor, same prize as GIBC V2's Grand Champion |
| [gridsense.md](gridsense.md) | Global Tech Innovation Challenge | Grand Prize Champion | Same event shape: international online student hackathon |
| [accesslens.md](accesslens.md) | Global Builders Hackathon: Code for Impact | Global Impact Award (Grand Prize) | Same event shape; research-grounded, evidence-led writing |

A separate, non-winner scan of the **live GIBC V2 field** (competitors' public repos) is in [`../FIELD-SCAN.md`](../FIELD-SCAN.md). It turned out to be the single most decision-relevant piece of research.

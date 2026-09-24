# Winner brief: DebtShield

**Hackathon:** Warwick Finance Societies Fintech Hackathon ("The FinTech Hackathon"), 2026 · **Prize won:** Best Overall Hack + Best 'Financial Inclusion' Stream, per HackWinnerDB entry `debtshield` and the repo README ("Winner: Best Overall Hack & Best Financial Inclusion")
**Submission URL:** https://devpost.com/software/debtshield · **Repo:** https://github.com/JamieGuo7/Debt-Shield · **Demo video:** not viewable from this network
**Verified:** page loaded ☐ (blocked) · prize stated ☑ (HackWinnerDB + README) · video played ☐ · repo opened ☑

## Pitch, verbatim
> A browser extension powered by your Shield Score, intervening in real time as you spend to protect your savings.

README problem statement: "Modern e-commerce is designed to be frictionless, making it dangerously easy to spend impulsively without understanding the long-term effects. At the point of sale, customers only see their current balance, and not how it affects their cashflow in the future."

## The wow moment
At checkout the extension reads the cart total, **re-runs a Monte Carlo cash-flow simulation**, and shows how *this* purchase drops your probability of staying solvent (the "Shield Score") and delays your savings goal.

## Demo teardown
- Length / first 15 s: not viewable.
- Data: bank transactions imported by the user; the repo ships sample account CSVs.
- The model is simple and the framing is sharp: "Default Event" = projected cash below zero; Shield Score = P(no default) across simulated paths.

## Scope reality
- Working: data import and cleaning, Monte Carlo over 12-month paths, scoring, Chrome extension with checkout detection and a HUD, dashboard.
- Their "challenges" section is candid about hard parts (price detection across retailers; presenting probabilistic risk clearly).
- Commit window: 40 commits, Feb 28 → Mar 5 2026 (a 24 h event plus cleanup), 4-person team.

## Stack
Python (simulation, scoring), Chrome extension (JS), HTML dashboard. The stack wasn't the story; **probability made legible** was.

## Why this won (one sentence)
It turned an abstract risk model (P(solvent)) into a single number that changes at the exact moment a decision is made.

## Transferable to us
- **Copy:** make uncertainty legible at the decision point. Our intervals must read as "likely above the line / too close to call / likely below", not as ± jargon.
- **Copy:** explicitly defining the risk event ("Default Event = …") in plain words. We define "below the line" exactly as the federal rule does.
- **Note:** "Best Overall" went to a probabilistic model with honest framing, not to an LLM wrapper.

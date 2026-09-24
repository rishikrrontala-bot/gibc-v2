# CONCEPT: Withheld

**Event:** Global Innovation Build Challenge V2 · **Track:** 02 Applied (Finance) · **Builder:** Rishik Rontala (solo) · **Claimed:** Wed Sep 23 2026, 10:56 PM EDT

**One line:** *The federal College Scorecard withholds the earnings figure for 3 in 4 U.S. college programs. Withheld estimates it, with honest, calibrated uncertainty, and shows which side of the new federal earnings line each program likely falls on, before you borrow for it.*

**The problem:** a high-school senior comparing programs looks up what graduates earn and owe. For **181,758 of 233,979 programs (77.7 %)** the government's own data says `PrivacySuppressed`: the cohort is too small to publish. From July 2027 a new federal rule (the One Big Beautiful Bill Act's earnings test; ED's STATS / Earnings Accountability final rule, July 1 2026) cuts off federal student loans to programs whose graduates earn less than a typical high-school graduate. Families will borrow for programs without knowing which side of that line they're on.

**The user:** a student (and their parent) weighing a program and a loan, especially a certificate or small program at a community or career college, where suppression is most common. (A persona, not a real user.)

**What it does**
1. **Search any program** (school × field × credential), all 233,979 in the federal file.
2. **Published or withheld:** show the official number when it exists; when it's suppressed, show the model's **estimate with an 80 % interval**, labelled as an estimate every time.
3. **The line:** compare against the state's high-school earnings benchmark → *likely above / too close to call / likely below*.
4. **The loan:** turn the program's typical debt into a monthly payment and a debt-to-earnings ratio.
5. **Show the work:** a validation page with held-out accuracy vs. baselines, interval coverage by program size, and exactly where the model is least sure.

**Wow moment (first 15 s of the video):** a field of 233,979 dots, three-quarters grey. The fog lifts into estimates, the earnings line sweeps across, and one real certificate program lands "likely below the line".

**Method:** gradient-boosted quantile regression (median + 10th/90th percentiles) on program features (field, credential, institution control, state, cost, Pell share, size…). **Split-conformal calibration by program-size band**, so the 80 % intervals cover about 80 % on held-out programs *of the same size*. Institution-grouped cross-validation. Baselines: field × credential median, state × credential median, ridge regression. The browser runs the exported model in pure TypeScript, tested for parity against the Python pipeline.

**What it refuses to do:** it never reverse-engineers suppressed values (medians can't be differenced, and it never tries). It predicts from *other* programs' patterns, with intervals that stay wide where the data is thin. It isn't the official determination, and it isn't financial advice.

**Data:** U.S. Department of Education, College Scorecard (public domain), Field of Study and Institution files, via the GitHub mirror in [Amherst-Statistics/CollegeScorecard](https://github.com/Amherst-Statistics/CollegeScorecard) (updated Mar 18 2026), with provenance hashes.

**Stack:** Python (pandas, LightGBM or scikit-learn HistGradientBoosting) for training · Vite + TypeScript static site · Canvas/WebGL field view · Vitest + Playwright · GitHub Pages. No backend, no key.

Full scoring: `research/CONCEPTS.md` (B 4.65 · C 3.45 · A 2.04).

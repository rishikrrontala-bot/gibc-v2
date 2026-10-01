# Withheld model card

**Purpose:** research into missing college-program earnings information. **Author:** Rishik Rontala. **Build assistance:** OpenAI Codex. **Release:** 2026-10-01.

**Data:** U.S. Department of Education College Scorecard, official June 10, 2026 snapshot. Target: EARN_MDN_5YR, median earnings five years after completion. Federally aided graduate populations and historical measurement windows apply; consult the linked ED dictionary. No student-level records.

**Architecture:** three CPU LightGBM quantile regressors (.1/.5/.9), quantile sorting and size-band split-conformal expansion. Full configuration lives in `pipeline/train.py`; models are committed as plain-text LightGBM files. Browser outputs are precomputed from this fixed model.

**Predictors:** CIP field; broad CIP group; credential; state; control; log(1 + sum of available IPEDSCOUNT1/2). Missing numeric sizes remain missing. Categorical vocabulary is formed without looking at outcomes. IDs, earnings, debt and repayment fields are excluded as predictive features.

**Split:** OPEID6 institution-family groups, random state 42 for outer split and 43 for train/calibration split. One representative per OPEID6 × CIP × credential outcome. 22,975 train; 7,664 calibration; 8,723 test. No institution-family overlap. These are separate grouped holdouts, not five-fold cross-validation or longitudinal testing.

**Results:** overall test MAE $9,029.87; median absolute error $5,647.39; coverage 77.554%; mean width $26,179.17. Field × credential baseline MAE $10,247.57. See `public/data/metrics.json` for all baselines, calibration corrections and subgroup results. The test result was not used to refit or widen the model afterward.

**Policy:** display the official number where available. For PS records, display an estimate only if at least 30 unique training outcomes share its CIP field and credential. For non-PS missing records, display no estimate. Supported published test subset MAE $7,901.28 and coverage 78.863% on 6,827 records; this still does not validate hidden programs.

**Risks:** selection/covariate shift, correlated outcomes, sparse fields, privacy noise, cohort-vintage mismatch, noncausal comparisons, and inappropriate interpretation as personal financial advice. No formal guarantee of conditional coverage is made. See `LIMITATIONS.md`.

**Reproducibility:** exact input hashes and URLs in manifest; fixed split keys and per-test predictions committed; independent verification script; pinned Python dependencies. CPU training uses four threads. Run-specific time and library versions are recorded in generated metrics. Different supported CPU/library builds can introduce numerical variation.

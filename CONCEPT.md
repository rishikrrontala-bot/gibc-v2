# Withheld

**GIBC V2 — Track 02: Applied (Medical Technology & Finance)**

Explore missing college-program earnings with uncertainty visible from the first result.

The June 10, 2026 College Scorecard contains 194,211 program records: 137,408 suppress five-year earnings, 41,282 publish them and 15,521 lack values for other reasons. Counts are program records, not students.

Withheld pairs the official data with independently tested quantile-boosting estimates, target-80% intervals and a support-based abstention policy. It searches colleges, compares up to three programs, exports source-labelled CSVs, and offers hypothetical loan arithmetic. Every estimate remains visibly distinct from an official observation.

The main technical contribution is an end-to-end, reproducible uncertainty-focused workflow: public-data ingestion, pooled-outcome deduplication, institution-family holdouts, three quantile regressors, size-band calibration, measured baseline comparisons, and explicit abstention.

Validation is on published outcomes only. Overall test coverage is 77.554%, below target. We cannot establish accuracy or coverage on hidden values. This is a research prototype and is not financial advice or a federal eligibility determination.

**Changes from the earlier plan:** official current release replaces the old mirror; five-year target replaces four-year; no unsupported regulatory threshold; precomputed inference replaces in-browser model execution. Original concept comparison is retained in research/CONCEPTS.md as historical planning.

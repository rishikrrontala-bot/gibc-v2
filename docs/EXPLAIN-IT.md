# Withheld: explain it in plain language

**Twenty-second version:** Most college program records in our chosen public dataset do not publish five-year earnings. Withheld helps people explore that gap without hiding it. It distinguishes official data from estimates, shows uncertainty, and refuses to guess when there is too little comparable evidence.

**The moving parts:** Python reads two government files, joins the institution attributes and separates institution families into three groups. LightGBM learns patterns from the training group. Another group sets the uncertainty intervals. A final, untouched group measures errors. The result becomes static JSON that a TypeScript website searches, compares and explains. The loan calculator is ordinary fixed-rate amortization; no money is moved and no applicant is scored.

## Fifteen likely judge questions

1. **Why does this matter?** People encounter blank outcome fields when researching college programs. A blank can conceal uncertainty rather than explain it. This prototype makes the absence and the limits of an estimate visible. We have not established improved real-world decisions through user studies.
2. **What is novel?** The combined interface treats provenance, abstention and empirical uncertainty as primary interactions. The underlying boosting and conformal algorithms are established methods; we do not claim a new learning algorithm.
3. **Is this recovering private data?** No. It estimates a program-level statistic from public program attributes. A prediction is not the hidden government value or information about a particular person.
4. **Why 70.8%?** 137,408 PrivacySuppressed records divided by all 194,211 program records in the pinned release. Other missing values are counted separately. The denominator is not students.
5. **What is being predicted?** The five-year program median earnings field, in source reference dollars. Not an individual's future salary and not a current job-market offer.
6. **What enters the model?** Field, broad field, credential, state, institution control and log completions. Other earnings, debt and institution identifiers do not enter as predictors.
7. **How do you prevent leakage?** We deduplicate pooled outcomes and split by OPEID6 institution family, so campuses in the same family cannot cross fit, calibration and test sets. Baselines and support counts use training data only.
8. **Why three models?** The 10th and 90th quantiles form an initial interval; the 50th is its middle estimate. Quantile loss is designed to fit those different conditional percentiles.
9. **What does conformal calibration do?** On separate institutions, we measure how far each actual outcome lies outside its initial interval. A finite-sample quantile of those scores expands future intervals. We calibrate by completion-size group when the group has enough examples.
10. **Does 80% mean a guarantee here?** No. It is a target. Observed test coverage is 77.554%, and the suppressed population may differ systematically. Standard conformal guarantees depend on exchangeability assumptions we cannot establish for suppressed data.
11. **How well does the model work?** Test MAE is $9,029.87, compared with $10,247.57 for a field-and-credential median baseline. The average interval is $26,179.17 wide. Those numbers show both usefulness and substantial uncertainty.
12. **Why refuse some estimates?** Fewer than 30 training peers in the same field and credential triggers abstention. It is a simple evidence policy, not a proof that 30 makes an estimate reliable. Non-suppression missing outcomes are never filled.
13. **What about small programs?** Under-30-completion test programs have 74.632% coverage, below the overall result. Completions are not the earnings cohort. We publish this weakness rather than claim equal performance.
14. **Why not use an LLM or backend?** Structured numeric outcomes suit a reproducible tabular model. Precomputation makes a cold judge visit fast and independent of paid APIs. It also avoids sending college searches to a server.
15. **What would you do next?** Evaluate temporal generalization on another cohort, investigate missingness shift, compare stronger baselines, and conduct consent-based usability studies. Do not roll this into lending or personal financial advice without substantially different validation and oversight.

## A reliable live walkthrough

Open the home page, reveal the model's view, select Rutgers, inspect the Aerospace bachelor's estimate and its interval, expand the evidence explanation, change the loan amount, pin the program, filter for Computer and bachelor's, pin a published program, compare and export. Finish on The methodology, showing both the baseline improvement and the coverage shortfall. See the video script for exact wording.

AI assistance was used extensively and is disclosed. Read the pipeline and rehearse these answers in your own words. Do not claim to have interviewed users, created conformal prediction, or validated against hidden outcomes.

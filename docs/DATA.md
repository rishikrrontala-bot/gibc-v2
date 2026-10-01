# Data provenance

Withheld uses public, aggregate U.S. Department of Education College Scorecard data. It contains no student-level records. The frozen release is **June 10, 2026**.

- [Official data portal](https://collegescorecard.ed.gov/data/)
- [Field-of-study documentation](https://collegescorecard.ed.gov/files/FieldOfStudyDataDocumentation.pdf)
- [Data.gov catalog](https://catalog.data.gov/dataset/college-scorecard)
- [Exact download URLs and SHA-256 hashes](../public/data/manifest.json)

The catalog lists **Creative Commons Attribution (CC BY)**. Attribution: U.S. Department of Education, College Scorecard, June 10, 2026. Withheld transforms the data and adds independently generated estimates; ED does not endorse those estimates. Code is MIT; the underlying data and fonts retain their own licenses.

## Interpretation

The target is `EARN_MDN_5YR`, median earnings five years after completion. It describes a defined historical population in the source documentation, not every graduate, current salaries, or an individual's prospects. Published earnings are privacy-protected statistics and may contain differential-privacy noise. Dollar figures are kept in the source's inflation-adjusted reference dollars; they are not independently restated to 2026 dollars.

`PrivacySuppressed` and other missing values are kept distinct. Of 194,211 campus/program records, 41,282 have published outcomes, 137,408 are suppressed and 15,521 are otherwise unavailable. These are **program records, not people**. The model provides estimates for 50,042 suppressed records and abstains for 87,366. No non-suppression missing value is filled.

## Fields and transformations

| Input | Use |
|---|---|
| UNITID | Join institution attributes; navigate campuses, never a model feature |
| OPEID6 | Group institution families for train/calibration/test separation |
| CIPCODE | Four-digit program field; its two-digit prefix is an additional feature |
| CREDLEV | Credential category |
| STABBR | Institution state, joined from institution file |
| CONTROL | Public/private institution category |
| IPEDSCOUNT1, IPEDSCOUNT2 | Sum available nonnegative counts, then log1p for modeling |
| EARN_MDN_5YR | Training/evaluation target; original published observation retained |
| DEBT_ALL_STGP_ANY_MDN | Published median debt shown in the calculator; never a model feature |

Completions are a proxy for program size, **not** the earnings-cohort denominator. Earnings and debt can describe different cohorts and populations. The calculator is illustrative and cannot establish affordability or a causal return on investment.

Pooled outcome duplicates are grouped by OPEID6 × CIPCODE × CREDLEV for modeling, with a main-campus record preferred. All campus records remain browseable. There are 190,331 unique pooled program keys across the full input. All source columns, cleaning choices and exclusion logic can be inspected in [train.py](../pipeline/train.py).

## Shipped format

The manifest defines the compact row schema. Each state JSON contains arrays in this order: record ID, institution ID, field, credential, published earnings, published debt, middle estimate, lower interval, upper interval, training-peer support, completions and source status. Nulls stay null. IDs are unique within this frozen release and are not promised stable across future releases.

`schools.json`, `fields.json` and `credentials.json` supply display labels. `field-sample.json` contains a deterministic sample of 1,200 actual records for the landing-page visualization. Its vertical arrangement is decorative and is explicitly labelled as having no numeric meaning.

Run `python pipeline/fetch.py` to download the pinned archives with hash verification. Run `python pipeline/train.py` to recreate prepared data and the held-out report. See the README for pinned Python dependencies. Raw archives are excluded from version control; prepared data, models, split membership and test predictions are included.

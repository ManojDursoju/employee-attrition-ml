# Task 1 — Employee Attrition Data Audit & Exploration

## Executive summary
The source dataset contains 2,389 rows and 42 columns. The audit identified missingness, repeated employee-observation records, class imbalance, and candidate leakage fields. The original `df` remains unchanged; justified changes were applied to `df_clean`.

## Target distribution
- Stayed: 2,040 (85.39%).
- Left within 12 months: 349 (14.61%).
- This is imbalanced. Later evaluation should include recall, precision, F1, ROC-AUC and PR-AUC.

## Missing values
- **resignation_date:** 2068 missing (86.56%).
- **exit_reason:** 2040 missing (85.39%).
- **exit_date:** 2040 missing (85.39%).
- **exit_interview_done:** 2040 missing (85.39%).
- **fnf_settlement_amount:** 2040 missing (85.39%).
- **months_since_last_promotion:** 1459 missing (61.07%).
- **last_engagement_score:** 528 missing (22.10%).
- **last_raise_pct:** 202 missing (8.46%).
- **last_performance_rating:** 182 missing (7.62%).
- **commute_distance_km:** 55 missing (2.30%).
- **highest_education:** 15 missing (0.63%).

Ordinary numeric gaps are not globally imputed in the audit. Imputers must be fitted on training data only. Exit-related fields remain in the audit but are excluded from early-warning predictors. Promotion-recency missingness is structurally meaningful when promotions_received is zero; `never_promoted` preserves this meaning.

## Duplicate records
Exact full-row duplicates in source: 0. Repeated employee groups: 6. Groups identical apart from `row_id`: 6. Duplicate copies removed from the audit-cleaned copy: 6. Confirm the one-record-per-employee-observation assumption with the data owner.

## Outlier comparison
- **annual_fixed_pay:** IQR flagged 93 (3.90%); z-score flagged 26 (1.09%).
- **avg_hours_worked_3m:** IQR flagged 48 (2.01%); z-score flagged 15 (0.63%).
- **tenure_months:** IQR flagged 73 (3.06%); z-score flagged 45 (1.89%).

IQR and z-score flags are not proof of errors. Negative tenure values were set to missing under the rule that tenure cannot be negative. Other flagged values are retained unless source validation proves them invalid.

## Leakage risks
See `leakage_review.csv`. Exit dates, resignation dates, exit reason, exit-interview status and final settlement amount are excluded from early-warning predictors. `dept_attrition_rate_prior_12m` remains excluded until its temporal construction is verified.

## Decisions and limitations
- **months_since_last_promotion** — Preserved NaN in audit copy; created never_promoted indicator (rows affected: 1459).
- **highest_education** — Filled with Unknown (rows affected: 15).
- **tenure_months** — Set to NaN pending source correction; no global imputation (rows affected: 4).
- **employee-observation record** — Kept first copy in df_clean; preserved original df (rows affected: 6).

Confirm the duplicate-copy rule, feature definitions/ranges, the Unknown education category, and prediction-time availability with the data owner. The data dictionary contains definition placeholders that should be replaced with approved business definitions.

## Handoff to Task 2
Implement these decisions in a reusable, versioned feature pipeline. Split before fitting imputers/encoders; include tests, save/load checks, metadata, and Docker execution. Do not fit preprocessing on the full dataset.

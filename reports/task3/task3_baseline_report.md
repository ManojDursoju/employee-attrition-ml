# Task 3 — Attrition Baseline Report

## Objective
Compare a majority-class reference model with Logistic Regression and a shallow Decision Tree for predicting whether an employee leaves within 12 months.

## Data and validation
- Training rows: 1906
- Held-out test rows: 477
- Predictor count: 31
- Validation: 5-fold stratified cross-validation on the training split.
- Target: `left_within_12m` (1 = left within 12 months).

## Provisional model
Selected from training cross-validation: **Logistic Regression — unweighted**.

Cross-validation mean metrics:
- Precision (attrition): 0.403
- Recall (attrition): 0.086
- F1 (attrition): 0.140
- ROC-AUC: 0.705
- Average precision: 0.312

## Held-out test metrics
- Accuracy: 0.853
- Balanced accuracy: 0.553
- Precision (attrition): 0.500
- Recall (attrition): 0.129
- F1 (attrition): 0.205
- ROC-AUC: 0.683
- Average precision: 0.327

## Interpretation
Read precision and recall together. Higher recall means more actual leavers are identified, while higher precision means fewer flagged employees are false alarms. The appropriate balance depends on the cost and capacity of follow-up interventions. The model must not be used to make automatic employment decisions.

## Limitations and next steps
- The test split was already inspected during Task 2 in this combined notebook, so these results are not a pristine final benchmark.
- Confirm predictors are available at the intended prediction date and that no post-outcome information is present.
- Use temporal validation if the production use case predicts future periods.
- Review fairness, probability calibration, threshold selection, and performance drift before any operational use.

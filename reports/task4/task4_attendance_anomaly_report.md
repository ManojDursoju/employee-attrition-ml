# Task 4 — Attendance Anomaly Detection Report

## Objective
Identify unusual attendance patterns for human review using IQR flags and Isolation Forest.

## Data used
- Rows analyzed: 2383
- Numeric attendance features: 5
- Features: attendance_rate_3m, late_arrivals_3m, avg_overtime_hours_per_month_3m, unpaid_leave_days_6m, paid_leave_days_6m

## Results
- Rows flagged by rule-based checks: 585
- Rows flagged by Isolation Forest: 120
- Rows flagged by both approaches: 118
- Contamination setting: 5.0%

## Interpretation
These are candidate anomalies, not confirmed errors or misconduct. IQR flags are easy to explain but can flag valid extremes. Isolation Forest finds unusual combinations of numeric values but does not explain cause.

## Limitations and next steps
- Confirm each attendance field definition, unit, valid range, and reporting period.
- Review flagged records with a domain owner before taking action.
- If reviewed examples become available, measure precision and false-alarm rate on that reviewed sample.
- Consider employee-level history and seasonality if multiple time periods are available.
- Do not use anomaly flags alone for disciplinary or employment decisions.

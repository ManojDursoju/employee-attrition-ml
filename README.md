# Employee Attrition & Workforce Intelligence

**AI/ML Project | Python · Pandas · Scikit-learn · Jupyter · Docker**

GitHub Repository: https://github.com/ManojDursoju/employee-attrition-ml

## 1. Project Overview

Employee Attrition & Workforce Intelligence is a machine learning project designed to study employee data, understand factors associated with employee attrition, and identify unusual attendance patterns.

Employee attrition means employees leaving an organization. Understanding attrition can help HR teams identify workforce trends and plan employee retention strategies.

This project follows a structured workflow, starting with data auditing and progressing toward feature engineering, baseline modelling, evaluation, and attendance anomaly detection.

## 2. Project Objectives

- Understand the quality and structure of employee data.
- Identify missing values, duplicate records, outliers, and invalid values.
- Detect potential data leakage before training models.
- Prepare a reusable feature engineering pipeline.
- Establish baseline models for employee attrition prediction.
- Evaluate classification performance using appropriate metrics.
- Explore attendance anomaly detection.
- Maintain reproducible code and reports using GitHub and Docker.

## 3. Dataset Description

The project uses the CortexHR AI/ML dataset provided for the assignment.

The main training sheet is `attrition_dataset`.

| Dataset characteristic | Description |
|---|---|
| Original records | 2,389 rows |
| Original columns | 42 |
| Target variable | `left_within_12m` |
| Target meaning | Whether an employee leaves within 12 months |
| Dataset type | Structured tabular data |
| Data purpose | Employee attrition analysis and prediction |

The dataset contains employee-related information, including employment characteristics and other workforce features.

The assignment dataset contains synthetic data for development and evaluation.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and machine learning |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| SciPy | Statistical analysis |
| Scikit-learn | Preprocessing and machine learning |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualizations |
| Jupyter Notebook | Interactive analysis |
| Docker | Reproducible execution environment |
| Git | Version control |
| GitHub | Source code management and submission |

## 5. Project Workflow

### Task 1 — Data Audit and Exploration

**Objective:** Understand the dataset before building machine learning models.

The audit examines:

- Dataset dimensions and data types.
- Missing values and their distribution.
- Duplicate employee records.
- Outliers using the Interquartile Range (IQR) and Z-score methods.
- Invalid and impossible values.
- Target class distribution.
- Potential data leakage.
- Cleaning decisions and their justification.

The target distribution contains:

| Class | Records | Percentage |
|---|---:|---:|
| Stayed | 2,040 | 85.39% |
| Left within 12 months | 349 | 14.61% |
| Total | 2,389 | 100% |

The dataset is imbalanced because the number of employees who stayed is substantially greater than the number who left.

**Important findings:** The initial audit identified missing values, repeated records, four invalid negative-tenure values, and potential post-outcome leakage columns.

The cleaning process evaluates each issue individually rather than automatically removing all unusual values.

**Main files:**

- `notebooks/01_data_audit.ipynb`
- `src/audit/audit.py`
- `reports/task1_data_audit_report.md`
- `reports/tables/`

### Task 2 — Reusable Feature Pipeline

**Objective:** Prepare a consistent and reusable data preprocessing workflow for machine learning.

The planned pipeline includes:

- Handling missing numerical values.
- Handling missing categorical values.
- Scaling numerical features where appropriate.
- Encoding categorical features.
- Removing identifiers and unsuitable predictor columns.
- Excluding leakage-prone features.
- Creating useful derived features.
- Fitting preprocessing steps on training data only.
- Saving reusable pipeline components.

Potential engineered features include tenure in years and whether an employee's raise is overdue.

**Expected outcome:** A reusable pipeline that prepares data consistently for training and prediction.

**Current status:** Task-related report and artifact files exist in the repository. The final implementation and tests must be verified before this task is declared complete.

### Task 3 — Baseline Attrition Models

**Objective:** Establish a reliable performance baseline before trying more complex models.

The assignment specifies comparisons involving:

- An always-stays dummy classifier.
- Logistic Regression.
- A Decision Tree with a maximum depth of four.

The evaluation should use stratified five-fold cross-validation with random seed 42.

Important metrics include:

- ROC-AUC
- Precision
- Recall
- F1-score
- PR-AUC
- Confusion matrix

Because identifying employees who may leave is important, recall must be considered alongside precision. A high accuracy score alone is not sufficient for an imbalanced dataset.

The assignment also specifies a separate stratified 20% test set for later evaluation. This test set must remain untouched until the designated evaluation task.

**Current status:** Baseline reports and result files are present. Their numerical results and evaluation procedure should be checked before reporting final model performance.

### Task 4 — Attendance Anomaly Detection

**Objective:** Identify unusual attendance patterns that may require further investigation.

The assignment specifies Isolation Forest as the starting anomaly detection method.

The analysis considers attendance-related features such as:

- Unpaid absences.
- Attendance rate.
- Late arrivals.
- Absence streaks.
- Working hours.

The model should be evaluated using the supplied anomaly labels for measurement, not used to train an unsupervised detector.

Important metrics include precision, recall, and false-alarm rates.

An anomaly is a signal for review, not proof of employee misconduct.

**Current status:** Attendance anomaly report and supporting result files are present in the repository. Model behaviour, threshold selection, and evaluation results should be validated before claiming final completion.

## 6. Data Quality and Machine Learning Principles

The project follows these principles:

1. Investigate data quality before modelling.
2. Treat missing values according to feature type and context.
3. Distinguish genuine outliers from invalid data.
4. Remove exact duplicate rows where appropriate.
5. Prevent post-outcome information from entering model features.
6. Fit imputers, scalers, and encoders using training data only.
7. Evaluate imbalanced classification with more than accuracy.
8. Keep the final test set separate from model development.
9. Document assumptions and limitations.
10. Use model predictions as decision-support signals, not automatic employment decisions.

Age and gender must not be used as model inputs under the assignment's requirements.

## 7. Repository Structure

```text
employee-attrition-ml/
│
├── notebooks/
│   └── 01_data_audit.ipynb
│
├── src/
│   └── audit/
│       └── audit.py
│
├── reports/
│   ├── tables/
│   ├── task1_data_audit_report.md
│   ├── task2/
│   ├── task3/
│   └── task4/
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

The `notebooks/` directory contains interactive analysis.

The `src/` directory contains reusable Python code.

The `reports/` directory contains audit findings, evaluation reports, and supporting tables.

The `Dockerfile` defines the container environment.

The `requirements.txt` file lists Python dependencies.

The `.gitignore` file excludes selected local and sensitive files from Git.

## 8. How to Run the Project

### Prerequisites

Install:

- Python 3.11
- Git
- Docker Desktop
- Visual Studio Code (recommended)

### Step 1 — Clone the repository

```bash
git clone https://github.com/ManojDursoju/employee-attrition-ml.git
cd employee-attrition-ml
```

### Step 2 — Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Step 3 — Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### Step 4 — Prepare the dataset

Place the supplied Excel workbook at:

```text
data/raw/02_CortexHR_AI_ML_Dataset.xlsx
```

Ensure the workbook contains the `attrition_dataset` sheet.

The raw dataset is not included in this repository. Use the authorized assignment workbook.

### Step 5 — Run the notebook locally

```powershell
python -m jupyter lab
```

Open:

```text
notebooks/01_data_audit.ipynb
```

Select the correct Python environment and run the notebook cells.

### Step 6 — Build the Docker image

Ensure Docker Desktop is running, then execute:

```powershell
docker build -t employee-attrition-ml:1.0.0 .
```

### Step 7 — Run JupyterLab in Docker

From the project root in PowerShell:

```powershell
docker run --rm -it -p 8888:8888 -v "${PWD}\data:/app/data" -v "${PWD}\artifacts:/app/artifacts" -v "${PWD}\reports:/app/reports" employee-attrition-ml:1.0.0
```

Open the tokenized URL printed in the terminal and navigate to the notebook.

**Note:** The dataset must be present in the mounted local `data` directory. The Docker image must include the notebook and all required dependencies.

## 9. Version Control and GitHub

The project is maintained in GitHub:

https://github.com/ManojDursoju/employee-attrition-ml

Git is used to track changes, preserve project history, and manage task submissions.

Example workflow:

```bash
git status
git add .
git commit -m "Describe the completed change"
git push
```

For subsequent assignment tasks, create a separate branch and pull request according to the programme's submission requirements.

Raw datasets, virtual environments, secrets, and unnecessary generated files should not be committed.

## 10. Results and Evaluation

The initial dataset audit established the dataset size, target distribution, and data-quality issues requiring investigation.

The repository contains supporting reports for the baseline modelling and attendance anomaly tasks.

Final model performance should be reported only after verifying the actual evaluation outputs. Useful evidence includes:

- Cross-validation metrics.
- Confusion matrices.
- ROC and precision-recall curves.
- Error analysis.
- Anomaly detection precision and recall.
- Threshold selection and false-alarm analysis.

A baseline is a reference point for determining whether later models provide meaningful improvement.

## 11. Limitations

- The assignment uses synthetic data and does not establish real-world employee behaviour.
- Model predictions can be affected by missing data, imbalance, and feature quality.
- Correlation does not establish causation.
- An anomaly does not necessarily indicate an error or misconduct.
- Model metrics do not guarantee future performance.
- Fairness, explainability, and monitoring require additional validation before production use.

Any deployment or employment-related use would require appropriate privacy, security, fairness, and human-review safeguards.

## 12. Future Improvements

- Complete and test the reusable preprocessing pipeline.
- Validate baseline model metrics and thresholds.
- Improve anomaly detection through systematic evaluation.
- Add automated tests and continuous integration.
- Add model versioning and explainability.
- Implement monitoring for data drift.
- Document API and deployment procedures.
- Conduct fairness checks and publish model cards.

## 13. Conclusion

This project establishes a structured approach to employee data analysis and workforce intelligence.

It begins with data quality, documents important modelling risks, and creates a foundation for reusable preprocessing, baseline evaluation, and anomaly detection.

The objective is to build a reproducible, measurable, and responsible machine learning workflow rather than relying on a model score alone.

---

**Repository:** https://github.com/ManojDursoju/employee-attrition-ml

**Project:** Employee Attrition & Workforce Intelligence

**Technologies:** Python, Pandas, Scikit-learn, Jupyter Notebook, Docker, Git, GitHub

**Submission note:** Update this document as each task is completed and validated. Only report a task as complete when its required implementation, tests, results, and deliverables have been checked.

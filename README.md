# Diabetes Data Wrangling using Pandas

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-2.x-150458?logo=pandas&logoColor=white)

Real-world data cleaning project demonstrating data wrangling skills using Python.

## Description
This project applies data wrangling techniques to a diabetes dataset with missing values. The goal is to transform raw data into a clean and structured format suitable for analysis.

## Steps Performed
- Removed missing values (`dropna`)
- Renamed columns (German labels)
- Created new feature: Blutzucker_Kategorie
- Converted labels (0 → Nein, 1 → Ja)
- Selected relevant columns

## Dataset
https://www.kaggle.com/datasets/bhavyamotiyani/diabetes-dataset-with-missing-value-for-practice

## Output columns
| Column | Meaning |
|---|---|
| Alter | Age |
| Blutzucker | Plasma glucose (mg/dL) |
| Blutzucker_Kategorie | Normal (< 140) · Erhöht (140–199) · Sehr hoch (≥ 200) |
| BMI | Body-mass index |
| Blutdruck | Diastolic blood pressure |
| Diabetes | Ja / Nein |

## Tech Stack
- Python
- Pandas

## Result
Clean and structured dataset ready for analysis, saved as `diabetes_tidy.csv`.

## Run
```bash
pip install -r requirements.txt
python main.py
```
The dataset is downloaded automatically with `kagglehub` (you may need a Kaggle account / API token).



import os

import pandas as pd
import kagglehub

# Download dataset
path = kagglehub.dataset_download(
    "bhavyamotiyani/diabetes-dataset-with-missing-value-for-practice"
)

# Load dataset
df = pd.read_csv(os.path.join(path, "Diabetes Missing Data.csv"))

print("Before cleaning:", df.shape)

# Drop missing values
df = df.dropna()

print("After cleaning:", df.shape)

# Rename columns
df = df.rename(columns={
    "Glucose": "Blutzucker",
    "Diastolic_BP": "Blutdruck",
    "Age": "Alter",
    "Class": "Diabetes"
})

# Create new feature
# < 140 Normal, 140–199 Erhöht, >= 200 Sehr hoch (Glukose in mg/dL)
df["Blutzucker_Kategorie"] = pd.cut(
    df["Blutzucker"],
    bins=[float("-inf"), 140, 200, float("inf")],
    labels=["Normal", "Erhöht", "Sehr hoch"],
    right=False,
)

# Convert labels
df["Diabetes"] = df["Diabetes"].map({0: "Nein", 1: "Ja"})

# Select relevant columns
df = df[[
    "Alter",
    "Blutzucker",
    "Blutzucker_Kategorie",
    "BMI",
    "Blutdruck",
    "Diabetes"
]]

# Save cleaned dataset
df.to_csv("diabetes_tidy.csv", index=False)

print("Cleaning complete! Saved to diabetes_tidy.csv")
print(df.head())

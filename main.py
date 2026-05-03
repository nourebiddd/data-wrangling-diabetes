import pandas as pd
import kagglehub

# Download dataset
path = kagglehub.dataset_download(
    "bhavyamotiyani/diabetes-dataset-with-missing-value-for-practice"
)

# Load dataset
df = pd.read_csv(path + "/Diabetes Missing Data.csv")

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
df["Blutzucker_Kategorie"] = df["Blutzucker"].apply(
    lambda x: "Normal" if x < 140 else "Erhöht" if x < 200 else "Sehr hoch"
)

# Convert labels
df["Diabetes"] = df["Diabetes"].replace({0: "Nein", 1: "Ja"})

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

print("Cleaning complete!")

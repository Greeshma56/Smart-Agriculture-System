import pandas as pd

df = pd.read_csv("dataset/Crop_recommendation.csv")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nCrop Types:")
print(df['label'].unique())

print("\nNumber of Crop Types:")
print(df['label'].nunique())


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

df['label'].value_counts().plot(kind='bar')

plt.title("Crop Distribution")
plt.xlabel("Crop")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
print(df.describe())
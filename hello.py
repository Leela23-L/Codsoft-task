import pandas as pd

# Load dataset
df = pd.read_csv("customer_data.csv")

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicates
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicates
df = df.drop_duplicates().copy()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["City"] = df["City"].fillna("Unknown")
df["PurchaseAmount"] = df["PurchaseAmount"].fillna(
    df["PurchaseAmount"].mean()
)

# Correct data types
df["Age"] = df["Age"].astype(int)

# Display cleaned data
print("\nCleaned Data:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_customer_data.csv", index=False)

print("\nCleaned dataset saved successfully!")

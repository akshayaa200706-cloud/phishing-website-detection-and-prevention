import pandas as pd

# --------------------------------
# 1. Load Dataset
# --------------------------------

df = pd.read_csv("raw/phishing_dataset.csv")

print("Original Shape:", df.shape)

# --------------------------------
# 2. Check Missing Values
# --------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------
# 3. Clean URL
# --------------------------------

df["url"] = df["url"].astype(str).str.strip()

# --------------------------------
# 4. Remove Duplicate URLs
# --------------------------------

print("\nDuplicate URLs:", df["url"].duplicated().sum())

df = df.drop_duplicates(subset=["url"])

# --------------------------------
# 5. Handle Missing Values
# --------------------------------

numeric_columns = [
    "domain_age",
    "dns_resolvable",
    "num_ips",
    "ttl",
    "num_name_servers"
]

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# --------------------------------
# 6. Clean Labels
# --------------------------------

df["label"] = df["label"].astype(str).str.strip().str.lower()

print("\nLabel Values:")
print(df["label"].value_counts())

# --------------------------------
# 7. Convert Labels to Numbers
# --------------------------------

df["label"] = df["label"].map({
    "legitimate": 0,
    "phishing": 1
})

# Check whether any labels failed to convert
print("\nMissing Labels After Mapping:")
print(df["label"].isnull().sum())

# --------------------------------
# 8. Check Final Missing Values
# --------------------------------

print("\nFinal Missing Values:")
print(df.isnull().sum())

# --------------------------------
# 9. Check Final Shape
# --------------------------------

print("\nFinal Shape:", df.shape)

# --------------------------------
# 10. Save Cleaned Dataset
# --------------------------------

df.to_csv(
    "processed/phishing_cleaned.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
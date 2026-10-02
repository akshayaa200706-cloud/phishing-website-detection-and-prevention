import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------
# 1. Load Cleaned Dataset
# --------------------------------

df = pd.read_csv("processed/phishing_cleaned.csv")

print("Dataset Shape:", df.shape)

# --------------------------------
# 2. Label Distribution
# --------------------------------

print("\nLabel Distribution:")
print(df["label"].value_counts())

print("\nLabel Percentage:")
print(df["label"].value_counts(normalize=True) * 100)

# --------------------------------
# 3. Basic Statistics
# --------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------
# 4. Plot Label Distribution
# --------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(
    data=df,
    x="label"
)

plt.title("Legitimate vs Phishing URLs")
plt.xlabel("Label")
plt.ylabel("Number of URLs")

plt.savefig("images/class_distribution.png")

plt.show()

# --------------------------------
# 5. Correlation Matrix
# --------------------------------

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(14, 10))

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm",
    annot=False
)

plt.title("Feature Correlation Matrix")

plt.savefig("images/correlation_matrix.png")

plt.show()

print("\nFeature analysis completed successfully!")
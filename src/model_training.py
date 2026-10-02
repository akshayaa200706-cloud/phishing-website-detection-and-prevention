import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# --------------------------------
# 1. Load Cleaned Dataset
# --------------------------------

df = pd.read_csv("processed/phishing_cleaned.csv")

print("Dataset Shape:", df.shape)


# --------------------------------
# 2. Define Features
# --------------------------------

features = [
    "entropy",
    "url_length",
    "num_www",
    "ratio_digits_url",
    "num_subdomains",
    "length_hostname",
    "random_domain",
    "num_dots",
    "num_hyphens",
    "ratio_digits_host",
    "prefix_suffix",
    "num_question_mark",
    "num_eq",
    "domain_age",
    "dns_resolvable",
    "num_ips",
    "ttl",
    "num_name_servers"
]

X = df[features]
y = df["label"]


# --------------------------------
# 3. Train-Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# --------------------------------
# 4. Logistic Regression
# --------------------------------

logistic_model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(
        max_iter=1000,
        random_state=42
    ))
])

logistic_model.fit(X_train, y_train)

print("\nLogistic Regression trained successfully.")


# --------------------------------
# 5. Decision Tree
# --------------------------------

decision_tree_model = DecisionTreeClassifier(
    random_state=42
)

decision_tree_model.fit(X_train, y_train)

print("Decision Tree trained successfully.")


# --------------------------------
# 6. Random Forest
# --------------------------------

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

random_forest_model.fit(X_train, y_train)

print("Random Forest trained successfully.")


# --------------------------------
# 7. Save Models
# --------------------------------

joblib.dump(
    logistic_model,
    "models/logistic_regression.pkl"
)

joblib.dump(
    decision_tree_model,
    "models/decision_tree.pkl"
)

joblib.dump(
    random_forest_model,
    "models/random_forest.pkl"
)

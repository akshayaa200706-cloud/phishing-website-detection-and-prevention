import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)


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
# 3. Same Train-Test Split
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# --------------------------------
# 4. Load Trained Models
# --------------------------------

logistic_model = joblib.load(
    "models/logistic_regression.pkl"
)

decision_tree_model = joblib.load(
    "models/decision_tree.pkl"
)

random_forest_model = joblib.load(
    "models/random_forest.pkl"
)


# --------------------------------
# 5. Create Model Dictionary
# --------------------------------

models = {
    "Logistic Regression": logistic_model,
    "Decision Tree": decision_tree_model,
    "Random Forest": random_forest_model
}


# --------------------------------
# 6. Evaluate Models
# --------------------------------

results = []

for name, model in models.items():

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    results.append({
        "Model": name,
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1 Score": f1
    })

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)

    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))
    print("F1 Score :", round(f1, 4))

    # --------------------------------
    # Confusion Matrix
    # --------------------------------

    cm = confusion_matrix(y_test, y_pred)

    print("\nConfusion Matrix:")
    print(cm)

    display = ConfusionMatrixDisplay(
        confusion_matrix=cm,
        display_labels=["Legitimate", "Phishing"]
    )

    display.plot()

    plt.title(f"{name} - Confusion Matrix")

    filename = name.lower().replace(" ", "_")

    plt.savefig(
        f"images/{filename}_confusion_matrix.png"
    )

    plt.close()


# --------------------------------
# 7. Create Results DataFrame
# --------------------------------

results_df = pd.DataFrame(results)

print("\n\nModel Comparison:")
print(results_df)


# --------------------------------
# 8. Save Results
# --------------------------------

results_df.to_csv(
    "reports/model_results.csv",
    index=False
)

print("\nModel evaluation completed successfully!")
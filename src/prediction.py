import os
import joblib
import pandas as pd

from feature_extraction import extract_features


# --------------------------------------------------
# Load Random Forest model
# --------------------------------------------------

MODEL_PATH = "models/random_forest.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Predict URL
# --------------------------------------------------

def predict_url(url):

    # Extract features from URL
    features = extract_features(url)

    # Convert dictionary to DataFrame
    feature_data = pd.DataFrame([features])

    # Make sure feature order matches training
    feature_data = feature_data[
        [
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
    ]

    # Prediction
    prediction = model.predict(feature_data)[0]

    # Probability
    probabilities = model.predict_proba(feature_data)[0]

    legitimate_probability = probabilities[0]
    phishing_probability = probabilities[1]

    # Convert prediction to label
    if prediction == 1:
        result = "PHISHING"
    else:
        result = "LEGITIMATE"

    return {
        "result": result,
        "legitimate_probability": legitimate_probability,
        "phishing_probability": phishing_probability,
        "features": features
    }


# --------------------------------------------------
# Test Prediction
# --------------------------------------------------

if __name__ == "__main__":

    test_url = "https://google.com"

    print("=" * 60)
    print("PHISHING WEBSITE DETECTION")
    print("=" * 60)

    print("\nTesting URL:")
    print(test_url)

    try:

        result = predict_url(test_url)

        print("\nPrediction:")
        print(result["result"])

        print(
            f"\nLegitimate Probability: "
            f"{result['legitimate_probability'] * 100:.2f}%"
        )

        print(
            f"Phishing Probability: "
            f"{result['phishing_probability'] * 100:.2f}%"
        )

        print("\nPrediction completed successfully!")

    except Exception as error:

        print("\nError:")
        print(error)
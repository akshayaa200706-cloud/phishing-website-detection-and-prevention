# 🛡️ Phishing Website Detection and Prevention Using Machine Learning

## 📌 Project Overview

Phishing websites are malicious websites designed to deceive users and steal sensitive information such as usernames, passwords, OTPs, banking details, and personal information.

This project develops a Machine Learning-based system to detect potentially phishing websites by analyzing URL and domain-related features.

The system classifies a website as either:

- 🟢 Legitimate
- 🔴 Phishing

It also provides a prevention-oriented Streamlit web interface that warns users when a suspicious website is detected.

---

## 🎯 Objectives

- Detect phishing websites using Machine Learning.
- Analyze URL and domain-based features.
- Compare multiple Machine Learning algorithms.
- Provide a user-friendly website detection interface.
- Warn users when a potentially phishing website is detected.
- Encourage users to avoid entering sensitive information on suspicious websites.

---

## 🧠 Machine Learning Algorithms

Three Machine Learning algorithms were implemented and compared:

1. Logistic Regression
2. Decision Tree
3. Random Forest

The models were trained using URL and domain-related features.

---

## 📊 Dataset

The dataset contains **60,000 website records** with URL and domain-related features.

### Important Features

- URL length
- URL entropy
- Number of subdomains
- Number of dots
- Number of hyphens
- Number of digits in URL
- Hostname length
- Domain age
- DNS resolvability
- Number of IP addresses
- TTL
- Number of name servers
- Prefix/suffix information
- Number of question marks
- Number of equal signs

### Target

| Label | Meaning |
|---|---|
| 0 | Legitimate |
| 1 | Phishing |

---

## 📈 Model Performance

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

### Results

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 98.48% | 99.58% | 97.53% | 98.55% |
| Decision Tree | 98.95% | 99.08% | 98.93% | 99.00% |
| Random Forest | 99.20% | 99.70% | 98.78% | 99.24% |

These results are based on the project's test split.

---

## 🛡️ Prevention System

The project also includes a Streamlit-based prevention interface.

When a URL is classified as phishing, the system displays a warning and advises the user:

- 🚫 Do not enter passwords.
- 🚫 Do not enter OTPs.
- 🚫 Do not enter banking information.
- 🚫 Do not share personal information.
- 🚪 Leave the suspicious website.

For websites classified as legitimate, the system provides a safety message while reminding users to remain cautious online.

---

## 🖥️ Application

The application is built using **Streamlit**.

### Main Features

- URL input
- Automated URL feature extraction
- Machine Learning prediction
- Phishing warning
- User safety recommendations
- Simple and user-friendly interface

---

## 📂 Project Structure

```text
phishing-website-detection-and-prevention/
│
├── app/
│   └── app.py
│
├── images/
│   ├── class_distribution.png
│   ├── correlation_matrix.png
│   ├── decision_tree_confusion_matrix.png
│   ├── feature correlation matrix.png
│   ├── legitimate vs phishing url.png
│   ├── logistic_regression_confusion_matrix.png
│   └── random_forest_confusion_matrix.png
│
├── models/
│   ├── decision_tree.pkl
│   ├── logistic_regression.pkl
│   └── random_forest.pkl
│
├── processed/
│   └── phishing_cleaned.csv
│
├── raw/
│   └── phishing_dataset.csv
│
├── reports/
│   └── model_results.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_analysis.py
│   ├── feature_extraction.py
│   ├── model_evaluation.py
│   ├── model_training.py
│   └── prediction.py
│
├── .gitignore
├── requirements.txt
└── README.md

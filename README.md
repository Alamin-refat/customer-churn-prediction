[![Live Demo](https://img.shields.io/badge/Live-Demo-red)](https://customer-churn-prediction-agehkjkylrehcwxvpncblh.streamlit.app/)

# 📊 Customer Churn Prediction: AI-Driven Retention Strategy

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-green.svg)]()
[![Model](https://img.shields.io/badge/Model-XGBoost-orange.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/Project-Complete-brightgreen.svg)]()

---

## 🎯 Project Overview
Customer churn prediction is a critical business problem in the telecom industry.  
This project presents an **end-to-end Machine Learning solution** that predicts whether a customer is likely to churn using historical customer behavior and service usage data.

The goal is to **maximize recall for churn customers**, ensuring that potential churners are identified early so that businesses can take **proactive retention actions**.

---

## 🚀 Live Demo

- **Streamlit Cloud:** https://customer-churn-prediction-agehkjkylrehcwxvpncblh.streamlit.app/
- **Hugging Face Spaces:** 

---

## ✨ Key Features
- **Real-time Churn Prediction:** Instant results with probability scores.
- **Risk Categorization:** Automatically flags 'High Risk' vs 'Low Risk' customers.
- **Interactive UI:** Built with Streamlit for a seamless user experience.
- **Proactive Strategies:** Provides business recommendations based on prediction results.

---

## 🧠 Technical Workflow
1. **Data Preprocessing:** Handled missing values, encoded categorical variables (One-Hot), and scaled numerical features.
2. **Imbalance Handling:** Utilized **SMOTE** (Synthetic Minority Over-sampling Technique) to balance the churn vs. non-churn classes.
3. **Model Selection:** Evaluated multiple algorithms, selecting **Gradient Boosting** for its superior Recall and Precision.
4. **Optimization:** Hyperparameter tuning to minimize False Negatives (missing a potential churner).

---

## 📊 Model Performance
The model focuses on **Recall** to ensure business stakeholders don't miss at-risk customers:

| Metric | Score |
| :--- | :--- |
| **Accuracy** | 76% |
| **Recall (Churn Class)** | ~70% |
| **ROC-AUC Score** | 0.83 |

---
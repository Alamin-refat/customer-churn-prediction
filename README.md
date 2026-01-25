<p align="center">
  <img src="assets/demo.gif" alt="App Demo" width="100%">
</p>

[![Live Demo](https://img.shields.io/badge/Live-Demo-red)](https://customer-churn-prediction-agehkjkylrehcwxvpncblh.streamlit.app/)

# 📊 Customer Churn Prediction: AI-Driven Retention Strategy

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Classification-green.svg)]()
[![Model](https://img.shields.io/badge/Model-Gradient%20Boosting-3498db.svg)]()
[![Library](https://img.shields.io/badge/Library-Scikit--Learn-F7931E.svg)](https://scikit-learn.org/)
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

## 🧪 Model Comparison & Selection
Multiple models were trained and evaluated, including:
- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

Gradient Boosting was selected as the final model due to:
- Superior recall for churn customers
- Strong ROC–AUC performance
- Better handling of non-linear relationships

---

## 🔍 Feature Importance
Understanding which factors drive customer churn is crucial for business strategy. Based on our model, the top 3 drivers are:
1. **Contract Type:** Month-to-month contracts have the highest churn risk.
2. **Tenure:** Newer customers are more likely to leave than long-term ones.
3. **Monthly Charges:** Higher bills correlate with increased churn probability.

---

## 🛠️ Tech Stack & Tools
The following technologies were used to build, evaluate, and deploy this project:

- **Programming Language:** Python 3.10+
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, XGBoost, Gradient Boosting
- **Class Imbalance Handling:** SMOTE (imbalanced-learn)
- **Model Deployment:** Streamlit (Frontend), Streamlit Cloud (Hosting)
- **Version Control:** Git & GitHub
- **Environment Management:** Virtualenv / Pip

---

## 📂 Project Structure

A quick overview of the directory structure to help you navigate the project:

```text
├── .streamlit/          # Streamlit configuration (Theme/UI)
├── app.py               # Main application script (Streamlit UI & Logic)
├── churn_model.pkl      # Saved Gradient Boosting model
├── scaler.pkl           # Saved StandardScaler for feature scaling
├── features.pkl         # List of feature names for consistency
├── requirements.txt     # List of Python dependencies
├── telco_churn.ipynb    # Jupyter Notebook (EDA & Model Development)
├── LICENSE              # MIT License file
└── README.md            # Project documentation
```

---

## 💻 Installation & Usage

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone [https://github.com/Alamin-refat/customer-churn-prediction.git](https://github.com/Alamin-refat/customer-churn-prediction.git)
cd Customer-Churn-Prediction
```
### 2. Create a Virtual Environment (Recommended)
This keeps the project dependencies isolated and prevents conflicts:
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Libraries
Install all necessary dependencies listed in the requirements file to ensure the environment is ready:
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Dashboard
Launch the web application locally to interact with the churn prediction model:
```bash
streamlit run app.py
```

---

## 🗺️ Future Roadmap

I plan to further enhance this project by implementing the following features:

- [ ] **Advanced Model Implementation:** Experiment with Deep Learning (ANN) and LightGBM to compare with current results.
- [ ] **Model Explainability:** Integrate **SHAP (SHapley Additive exPlanations)** values to show exactly why a specific customer is flagged as high risk.
- [ ] **Automated Retraining:** Build a pipeline to retrain the model automatically as new customer data becomes available.
- [ ] **Bulk Prediction:** Add a feature to upload a `.csv` file and get churn predictions for thousands of customers at once.
- [ ] **Customer Segmentation:** Use Clustering (K-Means) to group churners into different categories for personalized marketing.

---

## 📜 License

This project is licensed under the **MIT License**.

### What does this mean?
- **Personal & Commercial Use:** You can use this project for your own portfolio or business.
- **Modification:** You are free to modify the code and add new features.
- **Distribution:** You can share this project with anyone.

*For more details, please check the [LICENSE](LICENSE) file in this repository.*

---

## 📬 Contact & Connect

If you have any questions, feedback, or would like to discuss potential collaborations, feel free to reach out!

**Alamin Refat** *Aspiring Data Scientist & Machine Learning Enthusiast*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alaminrefat/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Alamin-refat)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:alaminrefat2017@gmail.com)

---
> **"Turning data into actionable insights, one model at a time."**



import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Customer Churn AI", page_icon="📊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; font-weight: bold; }
    .prediction-box { padding: 20px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD ASSETS ---
@st.cache_resource
def load_models():
    # Model files load
    model = pickle.load(open('churn_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
    features = pickle.load(open('features.pkl', 'rb'))
    return model, scaler, features

try:
    model, scaler, features_list = load_models()
except Exception as e:
    st.error(f"Error: Model files not found! Details: {e}")

# --- SIDEBAR INPUTS ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2636/2636330.png", width=100)
st.sidebar.title("Customer Profiling")

def user_input_features():
    # Numerical features
    tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)
    monthly_charges = st.sidebar.number_input("Monthly Charges ($)", 0.0, 150.0, 65.0)
    total_charges = st.sidebar.number_input("Total Charges ($)", 0.0, 9000.0, 500.0)
    
    # Categorical features based on your importance chart
    gender = st.sidebar.selectbox("Gender", ["Female", "Male"])
    contract = st.sidebar.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment = st.sidebar.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
    internet = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    paperless = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
    streaming = st.sidebar.selectbox("Streaming Movies", ["Yes", "No"])
    multiple = st.sidebar.selectbox("Multiple Lines", ["Yes", "No"])
    
    # Dictionary mapping (Must match training features)
    data = {
        'tenure': tenure,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'gender_Male': 1 if gender == "Male" else 0,
        'Contract_One year': 1 if contract == "One year" else 0,
        'Contract_Two year': 1 if contract == "Two year" else 0,
        'InternetService_Fiber optic': 1 if internet == "Fiber optic" else 0,
        'InternetService_No': 1 if internet == "No" else 0,
        'PaymentMethod_Credit card (automatic)': 1 if "Credit card" in payment else 0,
        'PaymentMethod_Electronic check': 1 if "Electronic check" in payment else 0,
        'PaymentMethod_Mailed check': 1 if "Mailed check" in payment else 0,
        'PaperlessBilling_Yes': 1 if paperless == "Yes" else 0,
        'StreamingMovies_Yes': 1 if streaming == "Yes" else 0,
        'MultipleLines_Yes': 1 if multiple == "Yes" else 0
    }
    return pd.DataFrame([data])

input_df = user_input_features()

# --- MAIN CONTENT ---
st.title("📊 Customer Churn Intelligence Dashboard")
st.markdown("Predicting churn probability using **Gradient Boosting AI**.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Selected Profile")
    st.write(input_df)

# --- DATA PREPROCESSING (The Fix) ---
# 1. Model exact features sequence maintain
final_df = pd.DataFrame(0, index=[0], columns=features_list)

# 2. columns update
for col in input_df.columns:
    if col in final_df.columns:
        final_df[col] = input_df[col].values[0]

# 3. Handle NaN/Null values
final_df = final_df.fillna(0)

# 4. Scaling (Numeric columns strictly transform)
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
final_df[num_cols] = scaler.transform(final_df[num_cols])

with col2:
    st.subheader("🔮 Prediction Analysis")
    if st.button("Analyze Risk"):
        # Prediction using aligned features
        prediction = model.predict(final_df[features_list])
        probability = model.predict_proba(final_df[features_list])[0][1] * 100
        
        if prediction[0] == 1:
            st.markdown(f"""<div class='prediction-box' style='background-color: #ffdce0; color: #ff4b4b;'>
                        HIGH RISK: {probability:.1f}% Probability</div>""", unsafe_allow_html=True)
            st.warning("**Retention Alert:** This customer shows high signs of leaving soon.")
        else:
            st.markdown(f"""<div class='prediction-box' style='background-color: #d4edda; color: #155724;'>
                        LOW RISK: {probability:.1f}% Probability</div>""", unsafe_allow_html=True)
            st.success("**Loyalty Insight:** This customer is likely to stay.")

# --- FOOTER ---
st.divider()
st.info("Built for Professional Portfolio | Model: Gradient Boosting | Data: Telco Churn Dataset")
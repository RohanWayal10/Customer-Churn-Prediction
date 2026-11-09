
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("customer_churn_model.pkl")

st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊"
)

st.title("Customer Churn Prediction")
st.write("Predict whether a telecom customer is likely to leave.")

st.subheader("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Partner", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (Months)", 0, 72, 5)
    phone = st.selectbox("Phone Service", ["Yes", "No"])
    multiple = st.selectbox(
        "Multiple Lines", ["Yes", "No", "No phone service"]
    )
    internet = st.selectbox(
        "Internet Service", ["DSL", "Fiber optic", "No"]
    )
    security = st.selectbox(
        "Online Security", ["Yes", "No", "No internet service"]
    )
    backup = st.selectbox(
        "Online Backup", ["Yes", "No", "No internet service"]
    )

with col2:
    protection = st.selectbox(
        "Device Protection", ["Yes", "No", "No internet service"]
    )
    support = st.selectbox(
        "Tech Support", ["Yes", "No", "No internet service"]
    )
    tv = st.selectbox(
        "Streaming TV", ["Yes", "No", "No internet service"]
    )
    movies = st.selectbox(
        "Streaming Movies", ["Yes", "No", "No internet service"]
    )
    contract = st.selectbox(
        "Contract", ["Month-to-month", "One year", "Two year"]
    )
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    payment = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )
    monthly = st.number_input(
        "Monthly Charges", min_value=0.0, value=90.0
    )
    total = st.number_input(
        "Total Charges", min_value=0.0, value=450.0
    )

if st.button("Predict Churn"):
    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple,
        "InternetService": internet,
        "OnlineSecurity": security,
        "OnlineBackup": backup,
        "DeviceProtection": protection,
        "TechSupport": support,
        "StreamingTV": tv,
        "StreamingMovies": movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    probability = model.predict_proba(customer)[0][1]

    if probability >= 0.5:
        st.error("Customer Likely to Churn")
    else:
        st.success("Customer Likely to Stay")

    st.metric(
        "Churn Probability",
        f"{probability * 100:.2f}%"
    )

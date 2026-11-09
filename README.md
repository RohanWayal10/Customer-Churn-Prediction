# 📊 Customer Churn Prediction

A Machine Learning project that predicts whether a telecom customer is likely to leave a service provider using customer demographics, account information, subscription details, and billing data.

The project includes data cleaning, exploratory data analysis, feature preprocessing, model training, evaluation, and an interactive Streamlit web application.

## 🎯 Project Objective

Customer churn is a major challenge for telecom companies. This project aims to identify customers who are likely to discontinue their services so businesses can take proactive retention measures.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Application:** Streamlit
- **Model Saving:** Joblib
- **Environment:** Jupyter Notebook

## 📁 Project Structure

```text
Customer-Churn-Prediction/
│
├───
WA_Fn-UseC_-Telco-Customer-Churn.csv
│
├─── customer_churn.ipynb
│
├── customer_churn_model.pkl
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 📂 Dataset

**Dataset:** IBM Telco Customer Churn

**Source:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

- Original dataset: 7,043 customer records.
- Records after cleaning: 7,032.
- Features: 19 input features.
- Target variable: Churn.
- Target classes: Yes (1) and No (0).

## 🔍 Project Workflow

1. Data loading and inspection.
2. Data cleaning and handling missing values.
3. Exploratory Data Analysis (EDA).
4. Churn distribution analysis.
5. Feature and target separation.
6. Train-test splitting with stratification.
7. Numerical and categorical preprocessing.
8. Model training and comparison.
9. Class imbalance handling.
10. Classification threshold tuning.
11. Final model evaluation.
12. Model serialization using Joblib.
13. Interactive Streamlit application.

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Balanced Logistic Regression

### Model Comparison

| Model | Accuracy | Churn Precision | Churn Recall | Churn F1 |
|---|---:|---:|---:|---:|
| Logistic Regression | 80.38% | 64.85% | 57.22% | 60.80% |
| Decision Tree | 73.06% | 49.34% | 49.73% | 49.53% |
| Balanced Logistic Regression | 72.57% | 49.00% | 79.70% | 60.70% |

### Final Model Performance

The final model uses a preprocessing pipeline with Balanced Logistic Regression and a classification threshold of 0.5.

| Metric | Result |
|---|---:|
| Accuracy | 72.57% |
| Churn Precision | 49% |
| Churn Recall | 79.70% |
| Churn F1-score | 60.70% |
| ROC-AUC | 83.51% |

**Confusion Matrix**

```text
[[723 310]
 [ 76 298]]
```

The model identified 298 out of 374 actual churn customers in the test dataset.

## 🌐 Streamlit Web Application

An interactive web application was developed using Streamlit.

Users can enter customer details and receive:

- Churn prediction.
- Churn probability.
- Customer risk indication.

### Run Locally

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Customer-Churn-Prediction
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Run the application**

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Application Testing

Three sample customer profiles were tested:

| Test Case | Churn Probability | Prediction |
|---|---:|---|
| High-risk customer | 88.90% | Likely to Churn |
| Low-risk customer | 1.23% | Likely to Stay |
| High-risk customer | 88.36% | Likely to Churn |

These are sample model predictions, not guaranteed real-world outcomes.

## 📌 Key Learnings

- Data cleaning and preprocessing.
- Exploratory Data Analysis.
- Handling class imbalance.
- One-hot encoding and feature scaling.
- Training and evaluating classification models.
- Understanding precision, recall, F1-score and ROC-AUC.
- Classification threshold tuning.
- Building an interactive ML application.

## ⚠️ Limitations

- The model is trained on a publicly available telecom dataset.
- Predictions are estimates and not guarantees.
- Performance on real-world customer data may differ.
- Further validation and model improvements are needed before business deployment.

## 👨‍💻 Author

**Rohan Wayal**

BE Information Technology Student

GitHub: [RohanWayal10](https://github.com/RohanWayal10)

---

⭐ If you find this project useful, consider giving the repository a star!

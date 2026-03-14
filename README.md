# Customer Churn Prediction using Machine Learning

## 📌 Project Overview

Customer churn is a major problem for many businesses. When customers stop using a product or service, it leads to revenue loss.

This project uses **Machine Learning** to predict whether a customer will churn based on their behavior and transaction history.

The model is trained on an **E-Commerce Customer Churn Dataset** and deployed using a **Streamlit web application** where users can input customer details and receive churn predictions.

---

## 🎯 Objectives

* Analyze customer behavior using data analysis techniques
* Build machine learning models to predict churn
* Compare model performance using evaluation metrics
* Deploy the model as an interactive web application

---

## 📊 Dataset

The dataset used in this project contains information about customer activity in an e-commerce platform.

### Important Features

* Tenure
* SatisfactionScore
* OrderCount
* CashbackAmount
* PreferredPaymentMode
* NumberOfDeviceRegistered
* DaySinceLastOrder

### Target Variable

`Churn`

* **0 → Customer stays**
* **1 → Customer leaves**

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit

---

## 📈 Project Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Train-Test Split
6. Handling Imbalanced Data using SMOTE
7. Machine Learning Model Training
8. Model Evaluation
9. Model Deployment using Streamlit

---

## 🤖 Machine Learning Models Used

* Logistic Regression
* Random Forest
* XGBoost

Among these models, **XGBoost performed the best and was selected for deployment**.

---

## 🖥️ Streamlit Web Application

The trained model is deployed using **Streamlit**.

The web application allows users to:

* Enter customer information
* Predict churn probability
* View churn analytics and charts

To run the app locally:

```
python -m streamlit run app.py
```

---

## 📂 Project Structure

```
Customer-Churn-Prediction
│
├── dataset
│   └── E Commerce Dataset.xlsx
│
├── notebooks
│   └── churn_analysis.ipynb
│
├── model
│   └── churn_model.pkl
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## 📊 Results

The machine learning model successfully predicts customer churn based on behavioral patterns.

Key insights from the dataset include:

* Customers with **low satisfaction scores are more likely to churn**
* Customers with **short tenure tend to leave earlier**
* Customers with **higher engagement are less likely to churn**

---

## 🚀 Future Improvements

* Deploy the application on cloud platforms
* Add more advanced models like Deep Learning
* Integrate real-time data pipelines
* Build a full business analytics dashboard

---

## 👨‍💻 Author

**Sara**
BCA Final Year Student
Machine Learning & Data Science Enthusiast

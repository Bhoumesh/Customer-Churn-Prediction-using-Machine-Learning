import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Customer Churn Prediction Dashboard")

st.write("Predict whether a customer will churn using Machine Learning.")

# Load dataset
df = pd.read_excel("E Commerce Dataset.xlsx", sheet_name="E Comm")

# Load trained model
model = pickle.load(open("churn_model.pkl", "rb"))

# Sidebar inputs
st.sidebar.header("Enter Customer Details")

tenure = st.sidebar.number_input("Tenure", 0, 100)
satisfaction = st.sidebar.slider("Satisfaction Score", 1, 5)
ordercount = st.sidebar.number_input("Order Count", 0, 50)
cashback = st.sidebar.number_input("Cashback Amount", 0, 500)

# Prediction button
if st.sidebar.button("Predict"):

    input_data = [[tenure, satisfaction, ordercount, cashback]]

    prediction = model.predict(input_data)

    if prediction == 1:
        st.error("⚠ Customer will CHURN")
    else:
        st.success("✅ Customer will STAY")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Chart section
st.subheader("Churn Distribution")

fig, ax = plt.subplots()
sns.countplot(x="Churn", data=df, ax=ax)
st.pyplot(fig)

# Tenure vs Churn
st.subheader("Tenure vs Churn")

fig2, ax2 = plt.subplots()
sns.boxplot(x="Churn", y="Tenure", data=df, ax=ax2)
st.pyplot(fig2)
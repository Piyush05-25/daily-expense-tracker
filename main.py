import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from expense_analysis import analyze_expenses
from predictor import predict_expenses

st.set_page_config(page_title="Daily Expense Tracker", layout="wide")

st.title("📊 Daily Expense Tracker & Analyzer")

uploaded_file = st.file_uploader("Upload your daily expenses CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])
    st.write("### Raw Data", df)

    # Show analysis
    analyze_expenses(df)

    # Show prediction
    days = st.slider("Predict days ahead", 1, 30, 7)
    predict_expenses(df, days)
else:
    st.info("Please upload a CSV file with 'Date', 'Category', 'Amount' columns.")
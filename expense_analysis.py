import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def analyze_expenses(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Week'] = df['Date'].dt.to_period('W').astype(str)

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Total Spending by Category")
    cat_sum = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
    st.bar_chart(cat_sum)

    st.subheader("Daily Spending Trend")
    daily = df.groupby('Date')['Amount'].sum()
    st.line_chart(daily)

    st.subheader("Weekly Spending")
    weekly = df.groupby('Week')['Amount'].sum()
    st.area_chart(weekly)
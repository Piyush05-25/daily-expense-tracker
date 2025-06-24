import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import streamlit as st

def predict_expenses(df, days):
    df['Date'] = pd.to_datetime(df['Date'])
    daily = df.groupby('Date')['Amount'].sum().reset_index()
    daily['Days'] = (daily['Date'] - daily['Date'].min()).dt.days

    model = LinearRegression()
    model.fit(daily[['Days']], daily['Amount'])

    future_days = np.array([daily['Days'].max() + i for i in range(1, days + 1)])
    predictions = model.predict(future_days.reshape(-1, 1))

    future_dates = pd.date_range(daily['Date'].max() + pd.Timedelta(days=1), periods=days)
    future_df = pd.DataFrame({'Date': future_dates, 'Predicted_Amount': predictions})

    st.subheader("Predicted Expenses")
    st.line_chart(future_df.set_index('Date'))
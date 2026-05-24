import streamlit as st

from services.fetch_data import fetch_market_data
from services.process_data import calculate_changes
from charts.plot_charts import (
    plot_gold_chart,
    plot_oil_chart,
    plot_currency_chart,
    plot_stock_chart
)

#Title of the dashboard
st.title("GeoPulse India")

st.write(
    "Real-time analysis of how global conflicts affect India's economy and markets. Stay informed with our comprehensive insights and visualizations."
)

#Fetching data
market_data = fetch_market_data()

#Processing data
processed_data = calculate_changes(market_data)

#Dislpay metrics
st.header("Live Market Metrics")

#create 4 columns for the metrics
col1, col2, col3, col4 = st.columns(4)

#Gold Price
col1.metric(
    "Gold Price",
    f"${processed_data['gold_price'].iloc[-1]:.2f}",
    f"{processed_data['gold_change'].iloc[-1]:.2f}%"
)

#Crude Oil Price
col2.metric(
    "Crude Oil Price",
    f"${processed_data['oil_price'].iloc[-1]:.2f}",
    f"{processed_data['oil_change'].iloc[-1]:.2f}%"
)

#Currency Exchange Rate
col3.metric(
    "USD/INR Exchange Rate",
    f"{processed_data['usd_inr'].iloc[-1]:.2f}",
    f"{processed_data['currency_change'].iloc[-1]:.2f}%"
)

#Stock Market Index
col4.metric(
    "Nifty 50 Index",
    f"{processed_data['nifty_price'].iloc[-1]:.2f}",
    f"{processed_data['nifty_change'].iloc[-1]:.2f}%"
)

# Display Charts
st.header("Market Trends")

# Gold chart
st.subheader("Gold Price Trend")
st.plotly_chart(plot_gold_chart(market_data))

# Oil chart
st.subheader("Crude Oil Price Trend")
st.plotly_chart(plot_oil_chart(market_data))

# Currency chart
st.subheader("USD/INR Exchange Rate Trend")
st.plotly_chart(plot_currency_chart(market_data))

# Stock chart
st.subheader("Nifty 50 Index Trend")
st.plotly_chart(plot_stock_chart(market_data))
import streamlit as st
import yfinance as yf
import pandas as pd

# Arranging the Streamlit application
st.set_page_config(
  page_title="Financial Asset Analaysis",
  layout="wide"
)

#Title
st.title("Financial Asset Analysis, Forecasting and Recommendation")

st.write(
  "Welcome to our financial asset analysis dashboard."
  "This application allows users to explore histroical stock prices and financial market trends."
)

# Financial asstets dropdown menu
stocks = {
  "Microsoft (MSFT)": "MSFT",
  "Viking Therapeutics (VKTX)": "VKTX",
  "Bloom Energy (BE)": "BE",
  "S&P 500 ETF (SPY)": "SPY",
  "Vanguard S&P 500 ETF (VOO)": "VOO"

}

selected_stock = st.selectbox(
  "Select a financial asset:",
  list(stocks.keys())
)

ticker = stocks[selected_stock]

# Now moving forward with downloading historical stock data
@st.cache_data(ttl=3600)
def load_data(symbol):
  data = yf.download(
    symbol,
    period="5y",
    auto_adjust=True,
    progress=False
  )
  return data

data = load_data(ticker)

# This will showcase the stock price chart
if not data.empty:
    st.subheader(f"{selected_stock} - Historical Closing Prices")

  # This will organize the columns for yfiance
    if isinstance(data.columns, pd.MultiIndex):
      data.columns = data.columns.get_level_values(0)

    st.line_chart(data["Close"])

    st.write("Historical stock data from Yahoo Finance.")

else:
  st.warning("No stock data is currently available.")

st.divider()
st.caption("MLSN Team 1 | University of California, Davis | Fall 2026")

    

import streamlit as st
import pandas as pd

st.set_page_config(page_title="NovaTrader BTC & Gold", layout="wide")

st.title("NovaTrader Gold & Bitcoin Dashboard")

df = pd.read_csv("trade_log.csv")
st.dataframe(df.tail(20))

buy_count = (df['Action'] == 'BUY').sum()
sell_count = (df['Action'] == 'SELL').sum()
st.metric("Buy Trades", buy_count)
st.metric("Sell Trades", sell_count)
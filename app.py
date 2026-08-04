import streamlit as st
from functions.plot import plot_ts

st.set_page_config(page_title="Stock Dashboard")

st.title("📈 Stock Dashboard")

ticker = st.text_input(
    "Digite o ticker da ação (ex: AAPL, TSLA, MSFT)",
    value="AAPL"
)

if ticker:
    fig = plot_ts(ticker)
    st.plotly_chart(fig, use_container_width=True)
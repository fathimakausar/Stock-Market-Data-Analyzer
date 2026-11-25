"""Optional Streamlit dashboard.  Run:  streamlit run app.py"""
import streamlit as st
from src.data_loader import load_stock_data
from src.cleaner import clean_data
from src.analysis import add_returns, add_moving_averages, add_volatility, summary_stats, find_crossovers
from src.backtest import sma_crossover_backtest

st.set_page_config(page_title="Stock Market Data Analyzer", layout="wide")
st.title("📈 Stock Market Data Analyzer")
st.caption("Educational project - not financial advice.")

ticker = st.sidebar.text_input("Ticker", "AAPL").upper()
start = st.sidebar.text_input("Start date", "2023-01-01")
use_csv = st.sidebar.checkbox("Use sample CSV (offline)", value=False)

if st.sidebar.button("Analyse"):
    raw, source = load_stock_data(ticker, start, None, "data/sample_stock.csv" if use_csv else None)
    df = add_volatility(add_moving_averages(add_returns(clean_data(raw))))
    st.write(f"**Source:** {source}")
    stats = summary_stats(df)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total return", f"{stats['Total Return %']}%")
    c2.metric("Volatility (ann.)", f"{stats['Annualised Volatility %']}%")
    c3.metric("Max drawdown", f"{stats['Max Drawdown %']}%")
    c4.metric("Risk level", stats["Risk Level"])
    st.subheader("Close price with SMA20 / SMA50")
    st.line_chart(df[["Close", "SMA20", "SMA50"]])
    st.subheader("Rolling volatility")
    st.line_chart(df["Rolling Volatility"])
    st.subheader("Daily returns (%)")
    st.bar_chart(df["Daily Return"] * 100)
    bt = sma_crossover_backtest(df)
    st.subheader("SMA crossover backtest vs buy & hold")
    st.line_chart({"Strategy": bt["equity"], "Buy & hold": bt["buy_hold"]})
    st.json({k: v for k, v in bt.items() if k not in ("equity", "buy_hold")})
    st.subheader("Crossover signals")
    st.dataframe(find_crossovers(df))
    st.subheader("All statistics")
    st.json({k: str(v) for k, v in stats.items()})
else:
    st.info("Choose a ticker in the sidebar and click **Analyse**.")

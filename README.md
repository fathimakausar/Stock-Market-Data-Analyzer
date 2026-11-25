# 📈 Stock Market Data Analyzer

A beginner-friendly Python project that fetches historical stock prices, cleans them, calculates returns,
moving averages and volatility, tests a simple SMA crossover strategy, draws charts and writes a final insights report.

> ⚠️ **Disclaimer:** This project is for **educational purposes only** and is **not financial advice**.
> `data/sample_stock.csv` contains **synthetic (made-up)** prices so the project runs offline.

## Problem Statement
Manually checking thousands of price rows is slow and error-prone. This tool automates trend, return and risk analysis for any stock.

## Industry Relevance
Brokerages, fintechs, equity-research teams and quant desks all rely on this pipeline:
**ingest → clean → indicators → risk → backtest → visualise → report.**
Useful for Python Developer, Data Analyst, Financial Analyst, Business Analyst and FinTech roles.

## Features
- Fetch data with **yfinance** (CSV fallback if offline)
- Data cleaning (types, duplicates, missing values)
- Daily & cumulative returns
- SMA20 / SMA50 / EMA20, golden & death cross detection
- Annualised volatility, Sharpe ratio, max drawdown, risk level
- Highest / lowest price analysis
- 7 charts saved as PNG
- SMA-crossover backtest vs buy & hold
- Text report + processed CSV
- Optional **Streamlit** dashboard

## Tech Stack
Python · Pandas · NumPy · Matplotlib · Seaborn · yfinance · Streamlit

## Folder Structure
```
Stock-Market-Data-Analyzer/
├── data/        sample_stock.csv (synthetic) + any CSVs you add
├── notebooks/   Jupyter experiments
├── src/         data_loader, cleaner, analysis, backtest, visualize, report
├── outputs/     processed CSVs
├── images/      generated charts
├── reports/     generated text reports
├── docs/        notes and screenshots
├── main.py      run the full pipeline
├── app.py       optional Streamlit dashboard
├── generate_sample_data.py
├── requirements.txt
└── .gitignore
```

## How to Run
```bash
python -m venv venv
venv\Scripts\activate            # Windows
source venv/bin/activate         # Mac/Linux
pip install -r requirements.txt

python main.py --ticker AAPL --start 2023-01-01          # live data from Yahoo Finance
python main.py --ticker DEMO --csv data/sample_stock.csv  # offline demo
streamlit run app.py                                      # optional dashboard
```
Indian stocks: use `.NS` (e.g. `TCS.NS`, `RELIANCE.NS`).

## Sample Output (synthetic demo data)
```
Total Return %            : 23.03
Annualised Volatility %   : 26.67   (MEDIUM risk)
Max Drawdown %            : -33.14
Current Trend             : UPTREND (price above SMA20 and SMA50)
17 SMA20/SMA50 crossover signals detected
```
*(The backtest starts after the 50-day warm-up, so its buy & hold figure differs slightly from total return.)*

## Screenshots
Add yours to `images/` and link them here:
`![Closing price](images/01_closing_price.png)`

## Learning Outcomes
Time-series handling with Pandas · financial metrics (returns, volatility, drawdown, Sharpe) · modular Python design ·
data visualisation · basic backtesting and look-ahead bias · Git/GitHub workflow.

## Future Improvements
RSI / MACD / Bollinger Bands · SQLite storage · FastAPI backend · Next.js dashboard · email/Telegram alerts · portfolio tracking.

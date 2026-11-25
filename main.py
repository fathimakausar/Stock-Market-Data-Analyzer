"""Stock Market Data Analyzer - run:  python main.py --ticker AAPL --start 2023-01-01
Educational project. NOT financial advice."""
import argparse
import os

from src.data_loader import load_stock_data
from src.cleaner import clean_data
from src.analysis import (add_returns, add_moving_averages, add_volatility,
                          find_crossovers, summary_stats)
from src.backtest import sma_crossover_backtest
from src import visualize as viz
from src.report import generate_report


def run(ticker, start, end, csv_path):
    print(f"\n[1/6] Loading data for {ticker} ...")
    raw, source = load_stock_data(ticker, start, end, csv_path)
    print(f"      Source: {source} | rows: {len(raw)}")

    print("[2/6] Cleaning data ...")
    df = clean_data(raw)
    print("      Missing values after cleaning:", int(df.isna().sum().sum()))

    print("[3/6] Calculating returns, moving averages, volatility ...")
    df = add_volatility(add_moving_averages(add_returns(df)))

    print("[4/6] Computing statistics and signals ...")
    stats = summary_stats(df)
    crossovers = find_crossovers(df)
    bt = sma_crossover_backtest(df)

    print("[5/6] Saving charts to images/ ...")
    for path in (viz.plot_close_price(df, ticker), viz.plot_moving_averages(df, ticker),
                 viz.plot_daily_returns(df, ticker), viz.plot_return_distribution(df, ticker),
                 viz.plot_volatility(df, ticker), viz.plot_volume(df, ticker),
                 viz.plot_backtest(bt, ticker)):
        print("      saved", path)

    print("[6/6] Writing report and CSV outputs ...")
    os.makedirs("outputs", exist_ok=True)
    df.to_csv(os.path.join("outputs", f"{ticker}_processed.csv"))
    crossovers.to_csv(os.path.join("outputs", f"{ticker}_crossovers.csv"))
    text, path = generate_report(ticker, source, stats, crossovers, bt)
    print("\n" + text)
    print(f"\nReport saved to {path}")


if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Stock Market Data Analyzer")
    p.add_argument("--ticker", default="AAPL", help="Ticker symbol, e.g. AAPL, TCS.NS, RELIANCE.NS")
    p.add_argument("--start", default="2023-01-01")
    p.add_argument("--end", default=None)
    p.add_argument("--csv", default=None, help="Use a CSV file instead of yfinance")
    a = p.parse_args()
    run(a.ticker.upper(), a.start, a.end, a.csv)

"""Creates data/sample_stock.csv with SYNTHETIC (made-up) prices so the project runs offline.
This is NOT real market data - it only exists to demo the pipeline."""
import numpy as np
import pandas as pd

np.random.seed(42)
dates = pd.bdate_range("2023-01-02", "2025-12-31")
returns = np.random.normal(0.0006, 0.017, len(dates))
close = 150 * np.cumprod(1 + returns)
open_ = close * (1 + np.random.normal(0, 0.004, len(dates)))
high = np.maximum(open_, close) * (1 + np.abs(np.random.normal(0, 0.006, len(dates))))
low = np.minimum(open_, close) * (1 - np.abs(np.random.normal(0, 0.006, len(dates))))
volume = np.random.randint(20_000_000, 90_000_000, len(dates))
df = pd.DataFrame({"Date": dates, "Open": open_, "High": high, "Low": low,
                   "Close": close, "Adj Close": close, "Volume": volume})
price_cols = ["Open", "High", "Low", "Close", "Adj Close"]
df[price_cols] = df[price_cols].round(2)
df.to_csv("data/sample_stock.csv", index=False)
print("Created data/sample_stock.csv with", len(df), "rows")

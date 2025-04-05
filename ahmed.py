import re
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("dark_background")

# Load stock symbols from Google Sheets
file_name = "https://drive.google.com/uc?export=download&id=1AmsQ95PffFlcoCkINd8iCxmLYdT1yIQJ"
df = pd.read_csv(file_name)

# Ensure 'Symbol' column exists
if 'Symbol' not in df.columns:
    raise ValueError("CSV file must contain a 'Symbol' column.")

# Extract and clean tickers
symbols = df["Symbol"].dropna().tolist()
filtered_tickers = [ticker for ticker in symbols if re.match(r'^[A-Z0-9]+$', ticker)]

# Download OHLC data
ohlc = yf.download(filtered_tickers, period="6mo")["Close"]

# Drop tickers with all NaNs
ohlc = ohlc.dropna(axis=1, how='all')

# Calculate 6-month return for each ticker
returns = (ohlc.iloc[-1] - ohlc.iloc[0]) / ohlc.iloc[0]

# Get top 25 tickers by return
top_25 = returns.sort_values(ascending=False).head(25)
print("Top 25 Tickers by 6-Month Return:")
print(top_25)

# Plot raw adjusted closing prices
plt.figure(figsize=(14, 8))
for ticker in top_25.index:
    plt.plot(ohlc[ticker], label=ticker)

plt.title("Top 25 Performing Stocks (Raw Adjusted Closing Prices - 6 Months)")
plt.xlabel("Date")
plt.ylabel("Adjusted Closing Price")
plt.legend(loc="upper left", fontsize='small', ncol=2)
plt.tight_layout()
plt.show()

# Plot normalized prices
plt.figure(figsize=(14, 8))
for ticker in top_25.index:
    normalized = ohlc[ticker] / ohlc[ticker].iloc[0]
    plt.plot(normalized, label=ticker)

plt.title("Top 25 Performing Stocks (6-Month Normalized Price)")
plt.xlabel("Date")
plt.ylabel("Normalized Price")
plt.legend(loc="upper left", fontsize='small', ncol=2)
plt.tight_layout()
plt.show()

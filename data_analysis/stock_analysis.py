import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

df = yf.download("TSM", start="2023-01-01", end="2023-12-31")
print(df.head())
print(df.info())
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
print(df.head())
print(np.diff(df["Close"])/df["Close"][:-1])
print((np.diff(df["Close"])/df["Close"][:-1]).mean())
print((np.diff(df["Close"])/df["Close"][:-1]).std())
print(((np.diff(df["Close"])/df["Close"][:-1]).mean() /
      (np.diff(df["Close"])/df["Close"][:-1]).std())*np.sqrt(252))

df["MA30"] = df["Close"].rolling(30).mean()
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Close"])
plt.plot(df.index, df["MA30"])
plt.xlabel("date")
plt.ylabel("prices(US dollars)")
plt.title("2023 TMC stock prices")
plt.tight_layout
plt.show()

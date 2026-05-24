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
# 最大回撤:從最高點跌到最低點，最多跌了幾％
rolling_max = df["Close"].cummax()
drawdown = (df["Close"]-rolling_max)/rolling_max
mdd = drawdown.min()
print(f"最大回撤：{mdd.values[0]:.2%}")

# squeeze可以有效壓縮至正確維度
drawdown_1d = drawdown.squeeze()
plt.figure(figsize=(12, 6))
plt.plot(df.index, drawdown_1d)
plt.fill_between(df.index, drawdown_1d, 0, alpha=0.3, color='red')
plt.ylabel("回撤")
plt.title("TSM 2023 回撤走勢")
plt.tight_layout()
plt.show()

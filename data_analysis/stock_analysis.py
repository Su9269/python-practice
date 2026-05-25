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
print(f"最大回撤：{mdd:.2%}")

# squeeze可以有效壓縮至正確維度
drawdown_1d = drawdown.squeeze()
plt.figure(figsize=(12, 6))
plt.plot(df.index, drawdown_1d)
plt.fill_between(df.index, drawdown_1d, 0, alpha=0.3, color='red')
plt.ylabel("回撤")
plt.title("TSM 2023 回撤走勢")
plt.tight_layout()
plt.show()

df["MA5"] = df["Close"].rolling(5).mean()
df["MA20"] = df["Close"].rolling(20).mean()
print(df[["Close", "MA5", "MA20"]].head(25))
# 當MA5從下穿上MA20，產生買入訊號
df["Signal"] = 0
df.loc[df["MA5"] > df["MA20"], "Signal"] = 1   # 1 = 持有
df.loc[df["MA5"] < df["MA20"], "Signal"] = -1  # -1 = 不持有

# 找出交叉點（訊號改變的地方）
df["Position"] = df["Signal"].diff()

# 買入點：從-1變成1
buy = df[df["Position"] == 2]
# 賣出點：從1變成-1
sell = df[df["Position"] == -2]

print(f"買入次數：{len(buy)}")
print(f"賣出次數：{len(sell)}")


df["MA30"] = df["Close"].rolling(30).mean()
plt.figure(figsize=(12, 6))
df["MA5"] = df["Close"].rolling(5).mean()
df["MA20"] = df["Close"].rolling(20).mean()
buy = df[df["Position"] == 2].dropna()
sell = df[df["Position"] == -2].dropna()
plt.plot(df.index, df["MA5"])
plt.plot(df.index, df["MA20"])
plt.plot(df.index, df["Close"], label="收盤價")
plt.scatter(buy.index, buy["Close"], marker="^",
            color="red", s=100, label="buy")
plt.scatter(sell.index, sell["Close"], marker="v",
            color="green", s=100, label="sell")
plt.xlabel("date")
plt.ylabel("prices(US dollars)")
plt.title("2023 TMC stock prices")
plt.tight_layout()
plt.show()

# 計算策略報酬率
df["Daily_Return"] = df["Close"].pct_change()
df["Strategy_Return"] = df["Daily_Return"] * df["Signal"].shift(1)

# 累積報酬率
cumulative_market = (1 + df["Daily_Return"]).cumprod()
cumulative_strategy = (1 + df["Strategy_Return"]).cumprod()

# 最終報酬率
print(f"買入持有報酬率：{cumulative_market.iloc[-1] - 1:.2%}")
print(f"均線策略報酬率：{cumulative_strategy.iloc[-1] - 1:.2%}")

plt.figure(figsize=(12, 6))
plt.plot(df.index, cumulative_market, label="買入持有")
plt.plot(df.index, cumulative_strategy, label="均線策略")
plt.legend()
plt.xlabel("date")
plt.ylabel("cumulative return")
plt.title("策略 vs 買入持有")
plt.tight_layout()
plt.show()

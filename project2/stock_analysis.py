import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

df = yf.download("2303.TW", start="2023-01-01", end="2023-12-31")
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
df = df.squeeze()
print(df.head())
# 計算每日報酬率
daily = np.diff(df["Close"])/df["Close"][:-1]
# 計算sharp ratio
print(f"sharp ratio 為{(daily.mean()/daily.std())*np.sqrt(252):.2f}")
# 計算MDD
MDD = ((df["Close"]-df["Close"].cummax())/df["Close"].cummax()).min()
print(f"MDD 為{MDD:.2%}")

df["MA5"] = df["Close"].rolling(5).mean()
df["MA20"] = df["Close"].rolling(20).mean()
df["signal"] = 0
# 持有
df.loc[df["MA5"] > df["MA20"], "signal"] = 1
# 不持有
df.loc[df["MA5"] < df["MA20"], "signal"] = 0
# 交叉點
df["position"] = df["signal"].shift(1).diff()
# 設置買賣點
buy = df[df["position"] == 1].dropna()
sell = df[df["position"] == -1].dropna()
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["MA5"], color="brown", label="MA5")
plt.plot(df.index, df["MA20"], color="orange", label="MA20")
plt.plot(df.index, df["Close"], color="green", label="stock prices")
plt.xlabel("date")
plt.ylabel("prices(NTD)")
plt.title("2303.TW STOCK LINE MA5 V.S MA20 AND CHANCE TO MAKE MONEY")
plt.scatter(buy.index, buy["Close"], marker="x",
            color="red", s=70, label="buy")
plt.scatter(sell.index, sell["Close"], marker="x",
            color="black", s=70, label="sell")
plt.tight_layout()
plt.legend()
plt.show()

# 計算策略報酬率
df["daily return"] = df["Close"].pct_change()
df["strategy return"] = df["daily return"]*df["signal"].shift(1)
# 累積報酬率
cumulative_normal = (1+df["daily return"]).cumprod()
cumulative_strategy = (1+df["strategy return"]).cumprod()
print(f"買入持有報酬率：{cumulative_normal.iloc[-1] - 1:.2%}")
print(f"均線策略報酬率：{cumulative_strategy.iloc[-1] - 1:.2%}")

plt.figure(figsize=(12, 6))
plt.plot(df.index, cumulative_normal, color="red", label="買入持有")
plt.plot(df.index, cumulative_strategy, color="black", label="均線策略")
plt.xlabel("date")
plt.ylabel("報酬率")
plt.title("策略比較")
plt.legend()
plt.tight_layout()
plt.show()

# 參數網格搜尋


def backtest_ma_strategy(df, short_window, long_window):
    df = df.copy()

    # 1. 算短期和長期均線
    df["MA_short"] = df["Close"].rolling(short_window).mean()
    df["MA_long"] = df["Close"].rolling(long_window).mean()

    # 2. 算signal（0/1，不是1/-1）
    df["signal"] = 0
    df.loc[df["MA_short"] > df["MA_long"], "signal"] = 1

    # 3. 算策略報酬率（記得shift避免Lookahead Bias）
    df["daily_return"] = df["Close"].pct_change()
    df["strategy_return"] = df["daily_return"] * df["signal"].shift(1)

    # 4. 算最終累積報酬率
    cumulative_strategy = (1 + df["strategy_return"]).cumprod()
    final_return = cumulative_strategy.iloc[-1] - 1

    return final_return


# 開始測試不同組均線造成的買賣效果哪一個最賺錢
short_windows = [5, 10, 15, 20]
long_windows = [20, 30, 60]

results = []

for short in short_windows:
    for long in long_windows:
        # continue 只跳過「這一輪」剩下的程式碼，但迴圈本身會繼續往下一輪跑
        if short >= long:
            continue
        final_return = backtest_ma_strategy(df, short, long)
        results.append({"short": short, "long": long, "return": final_return})

results_df = pd.DataFrame(results)
results_df = results_df.sort_values("return", ascending=False)
print(results_df)

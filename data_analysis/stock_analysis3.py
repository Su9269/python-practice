import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

df = yf.download("0050.TW", start="2024-01-01", end="2024-12-31")
df.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
df = df.squeeze()
# calculate daily profit
daily = np.diff(df["Close"])/df["Close"][:-1]
# caculate  sharpe ratio
sharpe_ratio = (daily.mean()/daily.std())*np.sqrt(252)
print(f"sharpe ratio is {sharpe_ratio:.2f}")
# caculate MDD
higest_price = df["Close"].cummax()
MDD = -max((higest_price-df["Close"])/higest_price)
print(f"MDD is {MDD:.2%}")

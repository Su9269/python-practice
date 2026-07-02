import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)     # 秀出所有列
pd.set_option('display.max_columns', None)  # 秀出所有欄
pd.set_option('display.max_colwidth', None)  # 秀出儲存格完整文字


data = {
    "customer": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"],
    "region": ["North", "North", "South", "South", "East", "East", "West", "West"],
    "sales": [1200, 800, 500, 1500, 300, 2000, 900, 400],
    "cost": [900, 500, 450, 1000, 250, 1200, 700, 350],
    "orders": [12, 8, 5, 15, 3, 20, 10, 4]
}

df = pd.DataFrame(data)
df.at[3, "sales"] = df["sales"].median()
df["profit"] = df["sales"]-df["cost"]
df["profit_rate"] = df["profit"]/df["sales"]
df["avg_order_value"] = df["sales"]/df["orders"]
df["high_value_customer"] = df["sales"] >= 1000
print(df)
print(df.groupby("region")[["sales", "cost", "orders", "profit", "profit_rate"]].aggregate(
    ["mean", "std", "median"]))
print(df[df["profit_rate"] > df["profit_rate"].mean()])

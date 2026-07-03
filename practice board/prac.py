import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)     # 秀出所有列
pd.set_option('display.max_columns', None)  # 秀出所有欄
pd.set_option('display.max_colwidth', None)  # 秀出儲存格完整文字


data = {
    "product": ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"],
    "category": ["Electronics", "Electronics", "Home", "Home", "Sports", "Sports", "Beauty", "Beauty", "Food", "Food"],
    "sales": [1200, 1800, 800, 900, 1500, 1000, 700, 600, 1100, 1300],
    "cost": [900, 1200, 500, 650, 1200, 700, 300, 350, 800, 900],
    "orders": [12, 18, 10, 8, 20, 12, 15, 10, 22, 26]
}

df = pd.DataFrame(data)
print(df.isnull().sum())
df["profit"] = df["sales"]-df["cost"]
df["profit_rate"] = df["profit"]/df["sales"]
df["avg_order_value"] = df["sales"]/df["orders"]
df["avg_order_profit"] = df["profit"]/df["orders"]
df["high_value_category"] = df["avg_order_value"] >= 100
df["high_profit_category"] = df["profit_rate"] >= 0.3


def range(x):
    return max(x)-min(x)


print(df)
print(df.groupby("category")[["sales", "profit", "profit_rate", "avg_order_value"]].aggregate(
    ["mean", "std", "median", "count", "max", "min", (range)]))

df.groupby("category")["profit_rate"].mean().plot(kind="bar", rot=45)
plt.xlabel("category")
plt.ylabel("prfoit_rate")
plt.tight_layout()
plt.show()

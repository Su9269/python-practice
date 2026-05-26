import matplotlib.pyplot as plt
import pandas as pd
import os
print(os.getcwd())
df = pd.read_csv("sales_data.csv")
print(df)
print(df.describe())
print(df.info())
print(df[df["profit"] < 0])
df["profit rate"] = df["profit"]/df["sales"]
print(df)

plt.hist(df["sales"])
plt.show()

plt.scatter(df["sales"], df["profit"])
plt.xlabel("sales")
plt.ylabel("profit")
plt.tight_layout()
plt.show()

print(df["sales"].corr(df["profit"]))
print(df["years"].corr(df["sales"]))

print(df.groupby("department")[["sales", "profit", "profit rate"]].mean())

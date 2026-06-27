import pandas as pd

data = {
    "employee": ["A", "B", "C", "D", "E", "F"],
    "department": ["Tech", "Tech", "HR", "HR", "Sales", "Sales"],
    "sales": [100, 300, 150, 500, 600, 700],
    "cost": [80, 240, 60, 480, 500, 350]
}

df = pd.DataFrame(data)
df["profit"] = df["sales"]-df["cost"]
df["profit rate"] = df["profit"]/df["sales"]
result = df.groupby("department")[
    ["sales", "profit", "profit rate"]].aggregate(["mean", "max", "min"])
print(result)
print(df[["employee", "profit rate"]].sort_values(
    "profit rate", ascending=False))

import matplotlib.pyplot as plt
import pandas as pd
pd.set_option('display.max_rows', None)     # 秀出所有列
pd.set_option('display.max_columns', None)  # 秀出所有欄
pd.set_option('display.max_colwidth', None)  # 秀出儲存格完整文字

data = {
    "employee": ["A", "B", "C", "D", "E", "F", "G"],
    "department": ["Tech", "Tech", "HR", "HR", "Sales", "Sales", "Sales"],
    "sales": [100, 300, 150, None, 600, 700, 200],
    "cost": [80, 240, 60, 200, 500, 350, 190]
}
df = pd.DataFrame(data)
df.at[3, "sales"] = df["sales"].median()
df["profit"] = df["sales"]-df["cost"]
df["profit_rate"] = df["profit"]/df["sales"]
print(df.groupby("department")[
      ["sales", "profit", "profit_rate"]].aggregate(["mean", "std", ("range", lambda x: x.max()-x.min())]))
data_list = [df.loc[df["department"] == "Tech", "profit_rate"], df.loc[df["department"]
                                                                       == "HR", "profit_rate"], df.loc[df["department"] == "Sales", "profit_rate"]]
color_list = ["red", "blue", "black"]
label_list = ["Tech", "HR", "Sales"]
plt.hist(data_list, label=label_list,
         color=color_list, edgecolor="white")
plt.legend()
plt.tight_layout()
plt.show()
print(df)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("NBA Player 202324 stats.csv")


def classify_player(row):
    tag = []
    if row["APG"] >= 6:
        tag.append("組織者")
    if row["RPG"] >= 7:
        tag.append("藍領苦工")
    if row["PPG"] >= 25:
        tag.append("得分手")
    if not tag:
        tag.append("路人")
    return ",".join(tag)


df["TYPE"] = df.apply(classify_player, axis=1)
# print(df["TYPE"].value_counts())
# print(df[df["NAME"].isin(["Nikola Jokic", "Luka Doncic"])]
#     [["NAME", "PPG", "RPG", "APG", "TYPE"]])

plt.figure(figsize=(10, 6))
df["TYPE"].value_counts().plot(kind="bar")
plt.xlabel("player type")
plt.ylabel("count")
plt.title("2023-24 the NBA player disstribution of type")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
# plt.show()

print(df.groupby("TYPE")[["PPG", "RPG", "APG"]
                         ].aggregate(["mean", "max", "min"]))

type_state = df.groupby("TYPE")["PPG"].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
type_state.plot(kind="bar")
plt.xlabel("player type")
plt.ylabel("PPG")
plt.title("the PPG of different type's player")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

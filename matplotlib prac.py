import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("NBA Player 202324 stats.csv")
top10 = df.nlargest(10, "PPG")
top10["NAME"] = top10["NAME"].str.replace("Shai Gilgeous-Alexander", "SGA")

allstar = df[(df["PPG"] > 20) & (df["RPG"] > 5) & (df["APG"] > 5)]
plt.figure(figsize=(10, 6))
plt.scatter(allstar["RPG"], allstar["APG"], s=allstar["PPG"]*10)
for _, row in allstar.iterrows():
    plt.annotate(row["NAME"], (row["RPG"], row["APG"]))
plt.xlabel("籃板(RPG)")
plt.ylabel("助攻(APG)")
plt.title("ALL-STAR")
plt.show()

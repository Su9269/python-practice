import pandas as pd

data = {
    "名字": ["freeman", "kim", "ohtani", "betts"],
    "打擊率": [.398, .250, .411, .302],
    "全壘打": [18, 5, 25, 12]
}

df = pd.DataFrame(data)
print(df[df["打擊率"] > .3].sort_values("全壘打", ascending=False))

df = pd.read_csv("NBA Player 202324 stats.csv")
print(df[["NAME", "TEAM", "PPG"]].sort_values("PPG", ascending=False).head(10))
print(df[(df["3PA"] > 100) & (df["3P%"] > 0.3)])
print(df["3P%"].describe)
print(df.groupby("POS")["PPG"].mean().sort_values(ascending=False))

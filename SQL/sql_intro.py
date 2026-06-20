import sqlite3
import pandas as pd
df = pd.read_csv("NBA Player 202324 stats.csv")
conn = sqlite3.connect("nba.db")
df.to_sql("players", conn, if_exists="replace", index=False)


query = "SELECT COUNT(DISTINCT TEAM) FROM players"
print(pd.read_sql(query, conn))
team_info = pd.DataFrame({
    "TEAM": ["Lal", "Phi", "Bos", "Den"],
    "CONFERENCE": ["West", "East", "East", "West"],
    "CITY": ["Los Angeles", "Philadelphia", "Boston", "Denver"]
})

team_info.to_sql("teams", conn, if_exists="replace", index=False)

query = """
SELECT players.NAME,players.TEAM,players.POS,players.PPG,teams.CONFERENCE,teams.CITY
FROM players
LEFT JOIN teams ON players.TEAM = teams.TEAM
ORDER BY players.PPG DESC
LIMIT 15
"""
result = pd.read_sql(query, conn)
print(result)

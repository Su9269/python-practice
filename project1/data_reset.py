import pandas as pd
df_basics = pd.read_csv("nba player 202425 stats total.csv")
df_advanced = pd.read_csv("nba player 202425 advanced stats.csv")
df_salary = pd.read_csv("nba player 202425 salary.csv")
df_playoff = pd.read_csv("nba team 202425 playoff.csv")

duplicated_players = df_basics[df_basics["Player"].duplicated(
    keep=False)]["Player"].unique()
# ~代表反轉:將不是重複的球員選出來、isin是看有沒有在裡面、|代表or
df_basics_clean = df_basics[~df_basics["Player"].isin(
    duplicated_players) | df_basics["Team"].isin(["2TM", "3TM"])]

# subset="Player":依照球員名字判斷重複
# keep="first":重複的只保留第一筆（也就是合計那筆）
df_advanced_clean = df_advanced.drop_duplicates(subset="Player", keep="first")

df_salary_clean = df_salary.drop_duplicates(subset="Player", keep="first")

# 將advanced的得分欄位"PER"改成和其他表格一樣的"PTS"，用rename函數，inplace是直接修改的意思
df_playoff.rename(columns={'TEAM': "Team"}, inplace=True)

# 用merge值數連結表格，用on來說要依照哪一個欄位合併，how是決定要取交集(inner)還是聯集(outer)
df_merge1 = pd.merge(df_basics_clean, df_advanced_clean,
                     on="Player", how="left")
df_merge2 = pd.merge(df_merge1, df_playoff,
                     on="Team", how="left")
df_nba = pd.merge(df_merge2, df_salary_clean,
                  on="Player", how="left")


# 看看基礎數據有但薪資沒有的球員
no_salary = df_nba[df_nba["Salary"].isna()]["Player"].tolist()


# 將資料裡面"Age"欄位是空的人刪掉
df_nba = df_nba.dropna(subset=["Age"])
df_nba = df_nba.drop(columns=["Team_y"])
df_nba = df_nba.rename(columns={"Team_x": "Team"})


print(df_nba.shape)

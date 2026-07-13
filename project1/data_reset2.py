import pandas as pd
df_nba = pd.read_csv("nba player 202425 stats merged.csv")

# 檢測缺playoff的資料
missing_platoff = df_nba[df_nba["PLAYOFF"].isnull()]
# 檢測缺salary的資料
missing_salary = df_nba[df_nba["Salary"].isnull()]


# 將薪水的$、，符號去掉，再轉為浮點數之後將薪水缺失值補齊
# 把salary從字串轉為數字，errors=coerce是當salary遇到缺值的時候會變NaN，不會直接報錯
df_nba["Salary"] = df_nba["Salary"].str.replace("$", "", regex=False)
df_nba["Salary"] = df_nba["Salary"].str.replace(",", "", regex=False)
df_nba["Salary"] = pd.to_numeric(df_nba["Salary"], errors="coerce")
original_salary = df_nba["Salary"].copy()
# 先透過pos將資料分組，然後根據組別將salary缺失值補上該組中位數，transfprm函數保證回傳的樣子會一樣，fillna函數確保只會填到缺失值
df_nba["Salary"] = df_nba.groupby("Pos")["Salary"].transform(
    lambda x: x.fillna(x.median()))
# 將缺失值補0
cols_to_fill_zero = ["3P%", "FT%", "2P%", "TS%", "FG%", "eFG%"]
df_nba[cols_to_fill_zero] = df_nba[cols_to_fill_zero].fillna(0)

# 用 .loc 精準定位到那一列、那些欄位，手動填入真實數字
df_nba.loc[df_nba['Player'] == 'Nikola Jović',
           ['PER', 'USG%', 'OWS', 'DWS', 'WS', 'WS/48', 'OBPM', 'DBPM', 'BPM', 'VORP', "TS%"]] = [13.8, 18.3, 1.2, 1.3, 2.5, 0.104, -0.3, 0.6, 0.3, 0.7, 0.595
                                                                                                  ]
df_nba = df_nba[df_nba['Player'] != 'Skal Labissière']
print(f"剩餘缺失值：\n{df_nba.isnull().sum()[df_nba.isnull().sum() > 0]}")
df_nba.to_csv("nba player 202425 stats clean.csv", index=False)
print("儲存完成")

## SQL 基礎
- 寫的順序：SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
- 執行順序：FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

### 環境設置
- 用 SQLite，Python 內建套件 sqlite3，不用額外安裝
- 把 DataFrame 寫進資料庫：
- df.to_sql("表名", conn, if_exists="replace", index=False)
- pd.read_sql(query, conn)
- 多行 SQL 用三引號 """...""" 寫，方便分行閱讀

### 基礎查詢(接在SELECT 欄位 FROM 表格)
- SELECT 欄位 FROM 表格 → 選資料，等於 Pandas 的 df["欄位"]
- WHERE 條件 → 篩選，等於 df[df["欄位"]>值]:SELECT 欄位1, 欄位2 FROM 表格 WHERE 條件
- ORDER BY 欄位 DESC/ASC → 排序，DESC是大到小，ASC是小到大（預設）
- LIMIT n → 只要前n筆，等於 .head(n)
- HAVING 條件→ 對 GROUP BY 結果篩選，WHERE 是篩原始資料，HAVING 是篩分組後的結果
```sql
SELECT TEAM, AVG(PPG) AS avg_ppg
FROM players
GROUP BY TEAM
HAVING AVG(PPG) > 8
```
- 子查詢 → WHERE 欄位 > (SELECT ... FROM ...) 先算括號內，再用結果篩外層
**WHERE**篩原始資料（GROUP BY之前）
**HAVING**篩分組結果（GROUP BY之後）

### 分組統計
- GROUP BY 欄位 → 分組，等於 Pandas 的 groupby()
- AVG()、COUNT()、SUM()、MAX()、MIN() → 統計函式，可以接在 SELECT 後面
- COUNT(DISTINCT 欄位) → 算不重複的數量，等於 .nunique()
- AS → 幫計算結果取別名，例如 AVG(PPG) AS avg_ppg
```sql
SELECT TEAM, AVG(PPG) AS avg_ppg
FROM players
GROUP BY TEAM
```

### JOIN（資料表合併）
- FROM 表A JOIN 另一張表 ON 表A.欄位 = 表B.欄位 → 合併兩張表
- **INNER JOIN**（預設的JOIN）→ 只保留兩邊都有對應資料的行（交集）
- **LEFT JOIN** → 左表全部保留，右表沒有對應資料就顯示 NULL/NaN
```sql
SELECT players.NAME, teams.CONFERENCE
FROM players
(LEFT)JOIN teams ON players.TEAM = teams.TEAM
```

### 子查詢（Subquery）
- 在 WHERE 或 SELECT 裡面再放一個 SELECT
- 篩選條件需要先經過一次計算才能得到（例如「高於平均」）
- 先算括號內層，再用結果篩外層
```sql
SELECT NAME, PPG
FROM players
WHERE PPG > (SELECT AVG(PPG) FROM players)
```
### CASE WHEN — 條件分類
- 用法：
```sql
CASE 
    WHEN 條件1 THEN 結果1
    WHEN 條件2 THEN 結果2
    ELSE 結果3
END AS 新欄位名
```
- 時機：要根據條件建立新的分類欄位
- 對照 Pandas：等同 if/elif/else 寫成的自訂函式 + .apply()
```sql
SELECT NAME, PPG,
CASE 
    WHEN PPG >= 25 THEN 'super-star'
    WHEN PPG >= 15 THEN 'main-player'
    ELSE 'bench'
END AS player_level
FROM players
```

### 重要提醒
- 拿到資料要先檢查合理性，不要照單全收（今天發現資料集GP場次偏低，是賽季初截斷的小樣本，不是完整賽季數據）
- SQL 跟 Pandas 邏輯高度重疊，只是語法不同，業界常常是「SQL撈資料 + Pandas做分析」搭配使用



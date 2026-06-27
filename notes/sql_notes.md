## SQL 基礎

### 環境設置
- 用 SQLite，Python 內建不用額外安裝
- 把 DataFrame 寫進資料庫：df.to_sql("表名", conn, if_exists="replace", index=False)
- 執行 SQL 查詢：pd.read_sql(query, conn)
- 多行 SQL 用三引號 """..."""寫，比較好讀

### 基礎查詢
- SELECT 欄位 FROM 表格 → 選資料，等於 Pandas 的 df["欄位"]
- WHERE 條件 → 篩選，等於 df[df["欄位"]>值]
- ORDER BY 欄位 DESC/ASC → 排序，DESC是大到小，ASC是小到大（預設）
- LIMIT n → 只要前n筆，等於 .head(n)
- HAVING 條件→ 對 GROUP BY 結果篩選，WHERE 是篩原始資料，HAVING 是篩分組後的結果
- 子查詢 → WHERE 欄位 > (SELECT ... FROM ...) 先算括號內，再用結果篩外層

### 分組統計
- GROUP BY 欄位 → 分組，等於 Pandas 的 groupby()
- AVG()、COUNT()、SUM()、MAX()、MIN() → 統計函式，可以接在 SELECT 後面
- COUNT(DISTINCT 欄位) → 算不重複的數量，等於 .nunique()
- AS → 幫計算結果取別名，例如 AVG(PPG) AS avg_ppg

### JOIN（資料表合併）
- JOIN 另一張表 ON 表A.欄位 = 表B.欄位 → 合併兩張表
- **INNER JOIN**（預設的JOIN）→ 只保留兩邊都有對應資料的行（交集）
- **LEFT JOIN** → 左表全部保留，右表沒有對應資料就顯示 NULL/NaN

### 重要提醒
- 拿到資料要先檢查合理性，不要照單全收（今天發現資料集GP場次偏低，是賽季初截斷的小樣本，不是完整賽季數據）
- SQL 跟 Pandas 邏輯高度重疊，只是語法不同，業界常常是「SQL撈資料 + Pandas做分析」搭配使用



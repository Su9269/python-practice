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

### row_number()分組
- 「分組」之後再各自重新數數，而且絕對不會產生重複的行號
```sql
ROW_NUMBER() OVER (
PARTITION BY 分組欄位決(定要在哪裡「重新數數」)
ORDER BY 排序欄位(決定依照什麼順序來排這個行號))
```
```sql
SELECT 
    name, department, salary,
    ROW_NUMBER() OVER (
        PARTITION BY department 
        ORDER BY salary DESC
    ) as rn
FROM employees;
```
- 這邊部門不一樣後rn會重新排



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
### 整理資料
- 用法:剔除完全相同的資料列，通常搭配 JOIN 使用
- 整行比對：資料庫會檢查 p 資料表中的「所有欄位」，只有當兩筆（或以上）記錄的所有欄位值完全一樣時，才會被視為重複並被刪除。
- 搭配 JOIN 使用：當資料表有多對一的關聯，且使用 JOIN 擴展資料時（導致主表 p 的內容在結果集中重複），此語法能將擴展出的重複主表資料去除。
```sql
SELECT DISTINCT p.*
FROM products p
JOIN categories c ON p.category_id = c.id
WHERE c.type = 'Electronics';
```

### Like
```sql
---用%
WHERE first_name LIKE 'Jo%'      -- 開頭是Jo，後面接任意字元、任意長度
WHERE first_name LIKE '%son'     -- 結尾是son，前面接任意字元
WHERE first_name LIKE '%an%'     -- 中間任何位置包含an
---用_(底線))
WHERE first_name LIKE '_ohn'     -- 第一個字元任意，後面固定是ohn（例如John）
WHERE first_name LIKE '_____h'   -- 剛好6個字元，最後一個固定是h
```

## CTE
- 用法:創立一個虛擬的表然後去比對，找出想要的值或是想要的欄位
```sql
with copy as(
    select id, recordDate, temperature, 
           date_sub(recordDate, interval 1 day) as yesterday 
    from Weather
)
select c.id as Id from copy as c
left join weather as w on c.yesterday = w.recordDate
where c.temperature > w.temperature
```
- **WITH ... AS (...)**：先建立一個暫時的、可重複使用的中間結果表，讓後面的查詢邏輯更清晰，不用把所有邏輯擠在一個巢狀子查詢裡
- **DATE_SUB(日期, INTERVAL 1 DAY)**：把日期往前推1天，算出「理論上的前一天」是幾號。這個算出來的日期,不保證資料表裡真的存在這一天的紀錄
- **為什麼一定要用LEFT JOIN,不能用INNER JOIN**：
   - 時間序列資料（例如股市、營業日紀錄）常常不是連續的日期（例如週末不開市、假日沒紀錄）
   - 如果用INNER JOIN，「找不到前一天紀錄」的列會直接被排除，你看不到這個過程，也可能誤判資料完整性
   - 用LEFT JOIN保留這些列，讓「找不到的前一天」欄位顯示NULL，更能反映真實情況
   - 之後在WHERE子句比較數值時（例如`c.temperature > w.temperature`），如果w那邊是NULL，比較結果會是「未知」，SQL自動視為不符合條件、篩掉——最終結果通常跟INNER JOIN一樣，但LEFT JOIN的過程更透明、更適合用來檢查資料完整性
- **實務應用場景**：金融/股票資料是最典型的例子。週一要比較「前一天」，但週日沒開市根本沒有資料，`DATE_SUB`算出來的「昨天」在資料庫裡是不存在的，這種情況一定要用LEFT JOIN處理，不能假設每一天都連續存在


### 重要提醒
- 拿到資料要先檢查合理性，不要照單全收（今天發現資料集GP場次偏低，是賽季初截斷的小樣本，不是完整賽季數據）
- SQL 跟 Pandas 邏輯高度重疊，只是語法不同，業界常常是「SQL撈資料 + Pandas做分析」搭配使用



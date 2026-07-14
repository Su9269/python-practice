import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 內建的微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示錯誤
df_nba = pd.read_csv("nba player 202425 stats clean.csv")
numeric_column = df_nba.select_dtypes(
    include="number").columns.drop(['Rk', 'Salary', 'PLAYOFF', 'Age'])
corr_matrix = df_nba[numeric_column].corr()
plt.figure(figsize=(16, 14))
sns.heatmap(corr_matrix, cmap="coolwarm", center=0)
plt.title('變數相關係數熱力圖')
# plt.show()

pca_column = df_nba.select_dtypes(include="number").columns.drop([
    "Rk", "Salary", "PLAYOFF", "Age"])
corr_matrix = df_nba[pca_column].corr()
# unstack() 把它「攤平」成一個一維的 Series，index 變成 (欄位A, 欄位B) 這種配對，方便你排序、篩選。
corr_pairs = corr_matrix.unstack()
corr_pairs = corr_pairs[corr_pairs < 1.0]
corr_pairs_sorted = corr_pairs.sort_values(ascending=False)
print(corr_pairs_sorted.head(20))

# bins=20 是說每張圖要切成 20 個區間去統計每個區間有多少筆資料落在裡面
key_cols = ['PTS', 'AST', 'TRB', 'MP', 'PER', 'WS']
df_nba[key_cols].hist(figsize=(12, 8), bins=20)
plt.tight_layout()
plt.show()

print(df_nba.groupby('Pos')[['PTS', 'AST', 'TRB', 'BLK']].mean())

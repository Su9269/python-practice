import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 內建的微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示錯誤
df_nba = pd.read_csv("nba player 202425 stats clean.csv")
pca_column = df_nba.select_dtypes(include="number").columns.drop([
    "Rk", "Salary", "PLAYOFF", "Age"])
standar_data = StandardScaler().fit_transform(df_nba[pca_column])

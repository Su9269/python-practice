import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 內建的微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示錯誤
df_nba = pd.read_csv("nba player 202425 stats clean.csv")
pca_column = df_nba.select_dtypes(include="number").columns.drop([
    "Rk", "Salary", "PLAYOFF", "Age"])
# 將要做pca的每一欄標準化
scaler = StandardScaler()
standar_data = scaler.fit_transform(df_nba[pca_column])

# 必須將PCA()存成pca，才可以得知計算的相關性質
pca = PCA()
# pca_result是單純的數字座標沒有任何意義
pca_result = pca.fit_transform(standar_data)

# 透過kaiser準則去決定要保留幾個特徵根
eigenvalues = pca.explained_variance_
n_components_kaiser = np.sum(eigenvalues > 1)
# 透過累積解釋變異量決定要留下幾個主成分
np.cumsum(pca.explained_variance_ratio_)

pca_final = PCA(n_components=5)
pca_result_final = pca_final.fit_transform(standar_data)


loadingS = pd.DataFrame(pca_final.components_.T, columns=[
                        f'PC{i+1}' for i in range(5)], index=pca_column)
print(loadingS)

# PCA主成分解讀(保留5個主成分，累積解釋變異量 84.4%)

# PC1：整體出場量/產出量，幾乎所有變數（MP, FG, FGA, PTS, WS...）皆為正值且權重相近，代表「球隊倚重的主力 vs 邊緣輪替球員」的光譜
# PC2：效率型 vs 數量型，正：FG%, eFG%, TS%, PER, WS/48, BPM(效率指標)、負：FGA, 3PA, TOV, AST（出手量/球權相關）代表「高效率、低使用量球員」對比「高出手量、高球權球員」
# PC3：外線射手 vs 內線苦工，正：3P, 3PA, 3P%（三分相關、負：ORB, BLK, TRB（籃板/阻攻相關），代表「埋伏射手型球員」對比「禁區籃板/防守型球員」
# PC4：球星型 vs 場次型角色球員，正：G, MP, PF（出賽時間長、犯規多）、負：Trp-Dbl, USG%, VORP, PER（球星級指標）代表「數據全面、球權集中的球星」對比「時間久但普通的角色球員」
# PC5：防守貢獻 vs 進攻球權需求，正：DBPM, BPM（防守正負值）、負：USG%（進攻球權使用率），代表「防守見長、球權需求低」對比「進攻主導、高使用率」球員
# 註：PC4、PC5解釋力較低（各約5%、4%），訊號相對前3個較模糊，與前面主成分略有重疊屬正常現象。

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
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


inertia_list = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    # kmeans.fit(pca_result_final)：讓模型對你的5維PCA座標做分群訓練
    kmeans.fit(pca_result_final)
    inertia_list.append(kmeans.inertia_)


plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia_list, marker='o')
plt.xlabel('K (群數)')
plt.ylabel('Inertia (群內誤差)')
plt.title('手肘法 - K值選擇')
# plt.show()

# n_clusters=k 是設定要分成幾群、random_state=42 是為了讓每次跑出來的隨機初始化結果一致（方便重現）
# n_init=10 是因為初始中心點是隨機選的，跑10次取最好的一次結果，避免運氣不好選到爛的起點
# 注意：輪廓係數至少要分2群才有意義,K=1沒辦法算


# fit_predict直接拿到每個球員（每一列）被分到哪一群（0/1/2/3），存成df_nba的新欄位Cluster
kmeans_final = KMeans(n_clusters=4, random_state=42, n_init=10)
clusterlabels = kmeans_final.fit_predict(pca_result_final)
df_nba["Cluster"] = clusterlabels
print(df_nba['Cluster'].value_counts())
print(df_nba['Cluster'].nunique())
# 看每一群在5個主成分上的平均值
cluster_summary = df_nba.groupby('Cluster')[
    [f'PC{i+1}' for i in range(5)]].mean() if 'PC1' in df_nba.columns else None

# pca_result_final[:, i]是用numpy的切片語法，取出「所有列、第i欄」，也就是取出每個球員在第i個主成分上的座標值。
# 迴圈跑5次，把PC1到PC5各自變成df_nba的新欄位。
for i in range(5):
    df_nba[f'PC{i+1}'] = pca_result_final[:, i]

cluster_summary = df_nba.groupby(
    'Cluster')[['PC1', 'PC2', 'PC3', 'PC4', 'PC5']].mean()
print(cluster_summary)
# 群0：穩定輪替的資深角色球員（出賽時間長，但非球星級別）
# 群1：板凳末端/邊緣球員（各項數據全面偏低，出賽機會少）
# 群2：聯盟頂級球星（整體產出量最高，各方面全面壓制其他群）
# 群3：效率型外線射手（效率高、三分準，但整體產出量不算頂尖）

# 舉例查詢，換成你認知的防守型球星
print(df_nba[df_nba['Player'].isin(['Rudy Gobert', 'Bam Adebayo'])]
      [['Player', 'Cluster', 'PC1', 'PC2', 'PC3', 'PC4', 'PC5']])


# 有標籤的資料，拿去train/test
df_train_full = df_nba[df_nba['PLAYOFF'].notnull()].copy()
# 沒有標籤的81筆，留到最後才用
df_predict_set = df_nba[df_nba['PLAYOFF'].isnull()].copy()
# select_dtypes(include='number')先抓出所有數值型欄位，再將不需要的欄位刪除
feature_cols = df_train_full.select_dtypes(
    include='number').columns.drop(['Rk', 'Salary', 'PLAYOFF', "Cluster", "PC1", "PC2", "PC3", "PC4", "PC5"])
# X是特徵矩陣，y是要預測的答案。
X = df_train_full[feature_cols]
y = df_train_full['PLAYOFF']
# 把487筆切成80%訓練、20%測試(test_size=0.2)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 建立隨機森林分類器，用訓練集去fit(學習)
rf_model = RandomForestClassifier(random_state=42, class_weight='balanced')
rf_model.fit(X_train, y_train)


# rf_model.predict(X_test)：把「沒看過的」98筆特徵餵給訓練好的模型，讓它預測PLAYOFF是0還是1
y_pred = rf_model.predict(X_test)

# accuracy_score(y_test, y_pred)：拿模型「猜的答案」跟「真正的答案」比對，算出整體猜對的比例
# classification_report：會給你更細緻的資訊，包含precision（精確率）、recall（召回率）、f1-score，不只是「猜對的比例」這麼粗略
# confusion_matrix：一個2x2的表格，讓你看到「模型把0猜成0、把0猜成1、把1猜成0、把1猜成1」各自的數量
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# feature_importances_是模型訓練完後,自動算出每個變數對「判斷結果」的貢獻程度
# pd.Series(資料, index=feature_cols)——pd.Series是pandas裡「一維帶標籤的資料」，跟你熟悉的DataFrame的「一欄」概念一樣。
# 這裡的用法是：把feature_importances_這串沒有名字的數字，跟feature_cols（你的38個欄位名稱）綁在一起，這樣你才知道「哪個分數對應哪個變數」，不然只看到一串數字，不知道第一個數字是Age還是PTS。
feature_importance = pd.Series(
    rf_model.feature_importances_,
    index=feature_cols
).sort_values(ascending=False)

print(feature_importance.head(10))

# df_predict_set[feature_cols]——從切出來的81筆「沒有PLAYOFF標籤」的資料裡，只取出跟訓練時一模一樣的38個特徵欄位。
X_predict = df_predict_set[feature_cols]
# 用已經訓練好的模型(predict)去做預測
predictions = rf_model.predict(X_predict)

df_predict_set['Predicted_PLAYOFF'] = predictions
print(df_predict_set[['Player', 'Team', 'Predicted_PLAYOFF']].to_string())

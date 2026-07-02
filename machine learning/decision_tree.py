import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("NBA Player 202324 stats.csv")


df["defender"] = ((df["BPG"] >= 1) & (df["DRtg"] <= 110)).astype(int)


X = df[["PPG", "RPG", "APG", "SPG", "USG%", "TS%"]]
y = df["defender"]

print(df["defender"].value_counts())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 決策樹
dt = DecisionTreeClassifier(
    max_depth=5, class_weight="balanced", random_state=42)
dt.fit(X_train, y_train)
dt_pred = dt.predict(X_test)

# 隨機森林
rf = RandomForestClassifier(
    n_estimators=100, class_weight="balanced", random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

print("=== 決策樹 ===")
print(confusion_matrix(y_test, dt_pred))
print(classification_report(y_test, dt_pred))

print("=== 隨機森林 ===")
print(confusion_matrix(y_test, rf_pred))
print(classification_report(y_test, rf_pred))


feature_names = X.columns
importances = rf.feature_importances_

# 排序
indices = np.argsort(importances)[::-1]

plt.rcParams['font.family'] = 'Microsoft JhengHei'
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_names)), importances[indices])
plt.xticks(range(len(feature_names)), [
           feature_names[i] for i in indices], rotation=45)
plt.title("Feature Importance - 預測防守組球員")
plt.tight_layout()
plt.show()

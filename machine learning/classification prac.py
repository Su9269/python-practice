from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("NBA Player 202324 stats.csv")
df_clean = df[df["GP"] > df["GP"].median()]

print(df_clean["DRtg"].describe())
# 定義「防守大鎖」：drtg<110
df_clean["biglock"] = (df_clean["DRtg"] <= 106).astype(int)
x = df_clean[["SPG", "BPG", "RPG"]]
y = df_clean["biglock"]
print(df_clean["biglock"].value_counts())

# 練模型去進行預測
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=666)
model = LogisticRegression(class_weight="balanced")
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(predictions)
print(y_test.values)

# 看看模型表現
accuracy = accuracy_score(y_test, predictions)
print(f"model's accuracy{accuracy:.2%}")
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

### 資料集不佳導致結果不如預期##

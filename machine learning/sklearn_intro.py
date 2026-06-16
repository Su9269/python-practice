import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("NBA Player 202324 stats.csv")
x = df[["PPG", "RPG", "APG"]]
y = df["VI"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(predictions[:5])
print(y_test[:5].values)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"MSE：{mse:.2f}")
print(f"R²：{r2:.2f}")

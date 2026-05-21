import numpy as np
prices = np.array([100, 102, 98, 105, 103, 107, 110, 108, 112, 115])
# broadcasting
print(np.diff(prices)/prices[:-1])
# 平均報酬率
print((np.diff(prices)/prices[:-1]).mean())
# 波動率
print((np.diff(prices)/prices[:-1]).std())
sharp_ratio = (np.diff(prices)/prices[:-1]
               ).mean()/(np.diff(prices)/prices[:-1]).std()
print(sharp_ratio)

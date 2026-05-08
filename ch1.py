# 1
import pandas as pd
numbers = range(1, 101)
total = 0
for i in numbers:
    total += i
print("final ans:", total)
# 2
nums = [10, 3, 25, 7, 18]
for i in nums:
    maxnum = nums[0]
    if i > maxnum:
        maxnum = i
print(i)
total_1 = 0
for i in nums:
    total_1 += i
print(total_1)
# 3
scores = [50, 30, 60, 60, 60]


def count_pass(scores):
    count = 0
    for i in scores:
        if i >= 60:
            count += 1
    return


print(count_pass(scores))
# 4

data = {
    "name": ["A", "B", "C", "D"],
    "score": [50, 80, 90, 30],
    "class": ["X", "X", "Y", "Y"]
}

df = pd.DataFrame(data)
print(df["score"] > 60)

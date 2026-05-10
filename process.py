# 1
import pandas as pd


def avg(scores):
    avg = sum(scores)/len(scores)
    return avg


myscore = [50, 80, 90, 100, 60]
print(avg(myscore))
# 2


def topscore(scores):
    top = 0
    for i in scores:
        if i > top:
            top = i
    return top


print(topscore(myscore))
# 3
student = {"Amy": 80, "John": 55, "Eric": 90}
avg_student = sum(student.values())/len(student)
under60 = []
for name, score in student.items():
    if score < 60:
        under60.append(name)
print(avg_student)
print(under60)

# for i in variables:
# 給一個迭代 對list裡的東西都造訪一遍的感覺
# if
# 後面接一個條件
# append
# list.append()在list裡面新增
# function
# def function():....一個函式
# return 在function的最後面 回傳一個值可以後的計算或print

df = pd.DataFrame({"team": ["A", "A", "A", "B", "B", "B"], "name": [
                  "Amy", "John", "Eric", "Tom", "Kevin", "Mary"], "score": [80, 50, 90, 40, 70, 60]})

print(df.groupby("team")["score"].mean())
print(df.groupby("team")["score"].agg(['mean', 'max', 'min']))
teamavg = df.groupby("team")["score"].mean()
print(teamavg[teamavg < 60])

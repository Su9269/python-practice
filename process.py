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

df = pd.DataFrame({"team": ["A", "A", "A", "B", "B"], "name": [
                  "Amy", "John", "Eric", "Tom", "Kevin"], "score": [80, 50, 90, 40, 70]})

print(df.groupby("team")["score"].mean())
print(df.groupby("team")["score"].agg(['mean', 'max', 'min']))
teamavg = df.groupby("team")["score"].mean()
print(teamavg[teamavg < 60])

print(df[df["score"] > 60])
print(list(filter(lambda x: x["score"] > 60, df.to_dict("records"))))
print(df[df["team"] == "B"])
print(df[(df["team"] == "B") & (df["score"] > 60)])
print(list(sorted(df["score"], reverse=True)))

myscore = [80, 50, 90, 40]


def scorefilter(scores):
    count = 0
    for i in scores:
        if i > 60:
            count += 1
    return count


print(scorefilter(myscore))

myclass = {"Amy": 80, "John": 55, "Eric": 90}
bestone = ""
bestscore = 0
for name, score in myclass.items():
    if score > bestscore:
        bestscore = score
        bestone = name
print(bestone)


score = [80, 50, 90, 40, 70]


def score_filter(scores):
    counthigh = 0
    countlow = 0
    for i in scores:
        if i > 60:
            counthigh += 1
        else:
            countlow += 1
    print(f"high:{counthigh},low:{countlow}")


score_filter(score)

students = {"Amy": 80, "John": 55, "Eric": 90, "Tom": 40}
avg = sum(students.values())/len(students)
fail_in_exams = []
for name, score in students.items():
    if score < avg:
        fail_in_exams.append(name)
print(fail_in_exams)


df2 = pd.DataFrame({"name": ["Amy", "John", "Eric", "Tom", "Kevin", "Mary", "David"], "team": ["A", "A", "B", "B", "B", "A", "C"], "score": [
    80, 50, 90, 40, 70, 85, 60], "salary": [50000, 40000, 90000, 35000, 60000, 70000, 45000]})
print(df2.groupby("team")["name"].count())
print(df2.sort_values("score", ascending=False).head(3))
print(df2.groupby("team")["score"].mean())
print(df2["salary"].mean())
print(df2[(df2["score"] < 60) & (df2["salary"] > 55000)])

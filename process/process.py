# 1
import matplotlib.pyplot as plt
import sqlite3 as SQL
import pandas as pd


myscore = [80, 50, 90, 40, 70]


def score_tidy(scores):
    avgs = sum(scores)/len(scores)
    abovecount = 0
    belowcount = 0
    for i in scores:
        if i > avgs:
            abovecount += 1
        else:
            belowcount += 1

    return abovecount, belowcount


print(
    f"'above_avg':{score_tidy(myscore)[0]},'below_avg':{score_tidy(myscore)[1]}")


students = {"Amy": 80, "John": 55, "Eric": 90, "Tom": 40}
avgs = (sum(students.values())/len(students))
print(avgs)
near_score = 100
near_one = ""
for name, score in students.items():
    if abs(score-avgs) < near_score:
        near_score = abs(score-avgs)
        near_one = name
print(f"{near_one}")


df2 = pd.DataFrame({
    "employee": ["Amy", "John", "Eric", "Tom", "Kevin", "Mary", "David", "Jenny", "Mike", "Cindy"],
    "department": ["Sales", "Sales", "Tech", "Tech", "Tech", "HR", "HR", "Sales", "Finance", "Finance"],
    "performance": [80, 50, 95, 40, 70, 85, 60, 75, 88, 45],
    "salary": [50000, 40000, 100000, 35000, 65000, 70000, 45000, 55000, 90000, 42000],
    "years": [2, 1, 5, 1, 3, 4, 2, 3, 6, 1]
})
print(df2["salary"].corr(df2["performance"]))
performence_mean = df2["performance"].mean()
performence_std = df2["performance"].std()
salary_mean = df2["salary"].mean()
salary_std = df2["salary"].std()
print(df2[df2["performance"] > performence_mean+(performence_std*1.5)])
print(df2[df2["performance"] < performence_mean-(performence_std*1.5)])
print(df2[df2["salary"] > salary_mean+(salary_std*1.5)])
print(df2[df2["salary"] < salary_mean-(salary_std*1.5)])

print(df2.groupby("department")["salary"].agg(["mean", "std"]))
print(df2.groupby("department")["performance"].agg(["mean", "std"]))

plt.hist(df2["salary"])
plt.show()

plt.scatter(df2["salary"], df2["performance"])
plt.xlabel("salary")
plt.ylabel("performance")
plt.show()

salary_mean = df2.groupby("department")["performance"].mean()
salary_mean.plot(kind="bar")
plt.xlabel("department")
plt.ylabel("performance")
plt.xticks(rotation=45)
plt.show()

plt.scatter(df2["years"], df2["performance"])
plt.xlabel("years")
plt.ylabel("performance")
plt.show()
print(df2["years"].corr(df2["performance"]))

# DAY1
# number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for i in number:
# print(i)

# print([i for i in number if i % 2 == 0])
# fruits = ["蘋果", "香蕉", "橘子"]
# for fruit in fruits:
# print(fruit)

# DAY2
# count = 10
# while count >= 0:
# print(count)
# count -= 1

# while True:
# num = int(input("請輸入一個數字(輸入0停止):"))
# if num == 0:
# break
# print(num)

# total = 0
# count_1 = 0
# while count_1 >= 0:
# count_1 += 1
# total += count_1
# if count_1 == 100:
# break
# print(total)

# print("final answer", total)
# DAY3
# 1
# for i in range(1, 10):
# for k in range(1, 10):
# print(i*k)

# 2
# candidate = []
# for i in range(1, 101):
# if i % 3 == 0:
# candidate.append(i)
# print(i)

# 3
# fruits = ["apple", "banana", "watermalon", "papaya"]
# for index, fruit in enumerate(fruits):
# print(index, fruit)

# DAY4
# 1
# Mydict = {"name": "su", "age": "22", "country": "new taipei city"}
# print(Mydict["name"])
# print(Mydict["age"])
# print(Mydict["country"])

# 2
# Mydict["email"] = "yanyusu29@gmail.com"
# print(Mydict)

# 3
# print(Mydict.keys())
# print(Mydict.values())

# DAY5
# 1
# score = {"a": 100, "b": 50, "c": 85, "d": 60, "e": 40}
# print(sum(score.values())/len(score))

# 2
# print(max(score, key=score.get))
# print(max(score.values()))
# for a, b in score.items():
# if b == max(score.values()):
# print(a)

# 3
# for name, s in score.items():
# print(f"{name}:{s}")

# DAY6
# myclass = {"a": {"math": 90, "english": 80, "science": 100}, "b": {"math": 10, "english": 30, "science": 70},
# "c": {"math": 50, "english": 80, "science": 80}}

# 1
# for name, score in myclass.items():
# print(f"{name}總分是:{sum(score.values())}")

# 2
# for name, score in myclass.items():
# print(f"{name}平均是:{sum(score.values())/len(score)}")

# 3
# bestman = ""
# bestavg = 0
# for name, score in myclass.items():
# if sum(score.values())/len(score) > bestavg:
# bestavg = sum(score.values())/len(score)
# bestname = name
# print(f"{name}有{bestavg}是這個世界上的王")

# DAY7
# 1
# def mybigone(a, b):
#    bignum = a
#   if b > bignum:
#      bignum = b
#     return b
# else:
#   return a
# print(mybigone(8, 10))

# 2
# def evennum(a):
#  if a % 2 == 0:
#     print(f"{a}is a evennumber")
# else:
#   print(f"{a}is an odd number")
# return
# evennum(10)

# 3
# def circlearea(r):
# s = r**2*3.14
# return s
# print(circlearea(10))

# DAY8
# 1
# def greeting(name, say="你好"):
#   print(f"嗨{name},{say}")
# greeting("國王")
# 得到"嗨國王，你好"

# 2
# myclass = [5, 8, 12, 25, 98, 99]
# def max_and_min(scores):
#   a = max(scores)
#  b = min(scores)
# return a, b
# result = max_and_min(myclass)
# print(f"最大值是{result[0]},最小值是{result[1]}")


# 3
# def evennum_filter(scores):
#   evennum = []
#  for i in scores:
#     if i % 2 == 0:
#        evennum.append(i)
# print(evennum)
# myscore = [10, 20, 60, 52, 33, 34, 31, 91]
# evennum_filter(myscore)

# DAY9
# 1
# myclass = {"a": {"math": 90, "english": 80, "science": 100}, "b": {"math": 10, "english": 40, "science": 70},
#         "c": {"math": 50, "english": 80, "science": 80}, "d": {"math": 50, "english": 80, "science": 65}, "e": {"math": 80, "english": 90, "science": 70}}
# for name, score in myclass.items():
# print("這是", name, "的成績單", "math的分數是:",
#      score["math"], "english的分數是:", score["english"], "science的分數是:", score["science"])


# def avgmachine(scores):
#   for name, score in scores.items():
#      print(f"{name}的平均是{sum(score.values())/len(score.values())}")


# avgmachine(myclass)


# def failer(scores):
# count = 0
#   for name, score in scores.items():
#      if sum(score.values())/len(score.values()) < 60:
#        count += 1
# return count


# print(f"班上有{failer(myclass)}個人平均不及格")


# def top(scores):
#   topname = ""
#  topscore = 0
# for name, score in scores.items():
#    avg = sum(score.values())/len(score.values())
#   if avg > topscore:
#      topscore = avg
#     topname = name
# return topname


# print(f"{top(myclass)}是班上平均最高的人")


# def last(scores):
#   lastname = ""
#  lastscore = 100
# for name, score in scores.items():
#    avg = (sum(score.values())/len(score.values()))
#   if avg < lastscore:
#      lastscore = avg
#     lastname = name
# return lastname


# print(f"{last(myclass)}是班上平均最低的人")


# def mathking(scores):
#   topmathguy = ""
#  topmathscore = 0
# for name, score in scores.items():
#    for subject in score:
#       mathscore = score["math"]
# if mathscore > topmathscore:
#  topmathscore = mathscore
# topmathguy = name
# return topmathguy


# print(f"{mathking(myclass)}是班上數學最高分")
# 各科以此類推

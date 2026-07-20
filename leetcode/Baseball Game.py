# You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
# You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:
# 1.An integer x.
# Record a new score of x.
# 2.'+'.
# Record a new score that is the sum of the previous two scores.
# 3.'D'.
# Record a new score that is the double of the previous score.
# 4.'C'.
# Invalidate the previous score, removing it from the record.
# Return the sum of all the scores on the record after applying all the operations.
# The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
class Solution(object):
    def calPoints(self, operations):
        final = []
        for i in operations:
            if i == "C":
                final.pop()
            elif i == "D":
                final.append(final[-1]*2)
            elif i == "+":
                final.append(final[-2]+final[-1])
            else:
                final.append(int(i))
        return sum(final)
# Input: ops = ["5","2","C","D","+"]
# Output: 30
# Explanation:
# "5" - Add 5 to the record, record is now [5].
# "2" - Add 2 to the record, record is now [5, 2].
# "C" - Invalidate and remove the previous score, record is now [5].
# "D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
# "+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
# The total sum is 5 + 10 + 15 = 30.
# 易犯的錯（自己踩過的坑）：
# 1.型態誤判：operations裡的元素全部都是「字串」型態，即使是代表數字的元素（例如"5"），也不是int型態
# 錯誤想法：if type(i) is int:這樣寫永遠不會成立，因為字串"5"的type是str不是int
# 導致：程式永遠走到其他分支，final list永遠是空的，之後遇到"C"執行pop()時，對空list做pop會直接報錯

# 2. 排除法（else兜底）解法：與其正面判斷「這是不是數字」，改成先判斷「這是不是C、D、+」這三種特殊指令，都不是的話，用else兜底代表「剩下唯一可能就是數字字串」，再用`int(i)`轉型別
# 這個技巧適用於：某種情況難以直接判斷型態/條件，但可以用「排除掉其他已知情況」的方式間接抓出來

# 這題本質上是Stack的延伸應用：
# final[-1]（取最後一個）、final[-2]（取倒數第二個），本質上跟Stack「只操作最上層元素」的精神一致
# 跟Valid Parentheses一樣，都是「根據當前遇到的符號，決定要push還是要基於已有的內容做運算後再push」

# 下次遇到類似題目可以聯想：Valid Parentheses（同樣是Stack應用）、任何「需要根據歷史紀錄計算/取消操作」的題型

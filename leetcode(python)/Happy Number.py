# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            # 1. 檢查這個 n 是不是之前出現過（代表進入無限循環）
            if n in seen:
                return False
            # 2. 如果沒出現過，就把現在的 n 記下來
            seen.add(n)
            n = sum(int(x)**2 for x in str(n))
        return True
# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

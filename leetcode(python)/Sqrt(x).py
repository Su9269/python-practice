# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator.
# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

# 方法1
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        left = 1
        right = x//2
        while left <= right:
            mid = (left+right)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 > x:
                right = mid-1
            else:
                left = mid+1

# 方法2:


class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        a = 1  # 代表前兩階 (初始為第 1 階)
        b = 2  # 代表前一階 (初始為第 2 階)

        # 從第 3 階數到第 n 階
        for i in range(3, n + 1):
            # 新的這一階 = 前兩階相加
            current = a + b

            # 把變數往後挪一步，準備算下一階
            a = b        # 舊的前一階，變成未來的「前兩階」
            b = current  # 當前算好的這一階，變成未來的「前一階」

        return b


# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

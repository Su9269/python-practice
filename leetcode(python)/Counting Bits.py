# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
# sol 1
class Solution(object):
    def countBits(self, n):
        final = []
        for i in range(n+1):
            num = 0
            temp = i
            while temp > 0:
                num += temp % 2
                temp = temp//2
            final.append(num)
        return final
# sol 2


class Solution(object):
    def countBits(self, n):
        final = [0]*(n+1)
        for i in range(1, n+1):
            final[i] = final[i >> 1]+(i & 1)
        return final
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

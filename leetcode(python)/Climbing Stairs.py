# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
import math


class Solution(object):
    def climbStairs(self, n):
        total_ways = 0
        for x in range(n+1):
            if (n - x) % 2 == 0:
                y = (n-x)//2
                permutations = math.factorial(
                    x + y) // (math.factorial(x) * math.factorial(y))
                total_ways += permutations
        return total_ways

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

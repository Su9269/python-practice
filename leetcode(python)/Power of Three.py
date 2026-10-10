# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3**x.

class Solution(object):
    def isPowerOfThree(self, n):
        while n > 0 and n % 3 == 0:
            n //= 3
        return n == 1

# Example 1:
# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:
# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

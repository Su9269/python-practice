# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2**x
# solution 1
class Solution(object):
    def isPowerOfTwo(self, n):
        x = 0
        while 2**x < n:
            x += 1
        return 2**x == n

# solution 2


class Solution(object):
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n-1)) == 0

# Example 1:
# Input: n = 1
# Output: true
# Explanation: 2**0 = 1

# Example 2:
# Input: n = 16
# Output: true
# Explanation: 2**4 = 16

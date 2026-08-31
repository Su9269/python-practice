# Given an integer n, return true if it is a power of four. Otherwise, return false.
# An integer n is a power of four, if there exists an integer x such that n == 4**x.
class Solution(object):
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n-1)) == 0 and (len(bin(n)) % 2 == 1)

# Example 1:
# Input: n = 16
# Output: true

# Example 2:
# Input: n = 5
# Output: false

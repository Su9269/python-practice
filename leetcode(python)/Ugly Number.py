# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
# Given an integer n, return true if n is an ugly number.
class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        prime_factor = [2, 3, 5]
        for i in prime_factor:
            while n % i == 0:
                n = n//i
        return n == 1

# Example 1:
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3

# Example 2:
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.

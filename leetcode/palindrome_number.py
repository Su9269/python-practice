# 2.Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
# sol 1
class Solution(object):
    def addDigits(self, num):
        while num > 9:
            new_num = [int(x) for x in str(num)]
            num = sum(new_num)
        return num
# sol 2


class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return 9 if num % 9 == 0 else num % 9
# Example 1:
# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2
# Since 2 has only one digit, return it.

# Example 2:
# Input: num = 0
# Output: 0

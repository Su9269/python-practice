# 3.Roman to Integer
class Solution(object):
    def romanToInt(self, s):
        roman_numbers = {'I': 1, 'V': 5, 'X': 10,
                         'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            curr = roman_numbers[s[i]]
            if i+1 < len(s):
                nex_val = roman_numbers[s[i+1]]
            else:
                nex_val = 0
            if curr >= nex_val:
                result += curr
            else:
                result -= curr
        return result
# Input: s = "III"
# Output: 3
# Explanation: III = 3.

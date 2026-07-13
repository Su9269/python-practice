# 1.Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# 2.Given an integer x, return true if x is a palindrome, and false otherwise.


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


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

# 4.Longest Common Prefix


class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(x)for x in strs)
        ans = ""
        for i in range(min_len):
            letter = strs[0][i]
            for word in strs[1:]:
                if word[i] != letter:
                    return ans
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

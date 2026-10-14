# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


class Solution(object):
    def reverseVowels(self, s):
        key = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        s = list(s)
        left = 0
        right = len(s)-1
        while left < right:
            while left < right and s[left] not in key:
                left += 1
            while left < right and s[right] not in key:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# Thevowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm"

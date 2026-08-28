# Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
class Solution(object):
    def titleToNumber(self, columnTitle):
        ans = 0
        for char in columnTitle:
            ans = ans*26+(ord(char)-ord("A")+1)
        return ans


# Example 1:
# Input: columnTitle = "A"
# Output: 1

# Example 2:
# Input: columnTitle = "AB"
# Output: 28

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.
class Solution(object):
    def plusOne(self, digits):
        nums = 0
        for i in range(len(digits)):
            nums += digits[i]*(10**(len(digits)-1-i))
        final = [int(x) for x in str(nums+1)]
        return final
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# split()不能用來拆單一數字字串：
# split()是依照「分隔符號」切割字串（例如逗號、空格），適合像"1,2,3".split(",")這種情境
# "124"這種字串裡沒有分隔符號可以切，"124".split()只會回傳整段['124']，不會拆成單一字元
# 想把字串拆成一個一個獨立字元，直接用list("124")即可，不需要分隔符號，因為字串本身就是可迭代的
# "124".split("")會直接報錯ValueError: empty separator，Python不允許用空字串當分隔符號

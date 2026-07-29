# Given two binary strings a and b, return their sum as a binary string.
class Solution(object):
    def addBinary(self, a, b):
        sum_a = 0
        sum_a_str = a[::-1]  # 把字串倒過來，例如 "10" 變成 "01"，這樣索引 0 剛好就是 2^0
        for i in range(len(a)):
            if sum_a_str[i] == "1":
                sum_a += 2**i
        sum_b = 0
        sum_b_str = b[::-1]
        for k in range(len(b)):
            if sum_b_str[k] == "1":
                sum_b += 2**k
        final = sum_a+sum_b
        # bin(final) 會得到像 "0b100" 的字串，[2:] 可以把前面的 "0b" 削掉
        return bin(final)[2:]
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

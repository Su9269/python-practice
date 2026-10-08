# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

# solution 1
class Solution(object):
    def hammingWeight(self, n):
        final = [int(x) for x in bin(n)[2:]]
        return sum(final)

# solution 2


class Solution(object):
    def hammingWeight(self, n):
        num = 0
        temp = n
        while temp > 0:
            num += (temp & 1)
            temp = temp >> 1
        return num

# Example 1:
# Input: n = 11
# Output: 3
# Explanation:
# The input binary string 1011 has a total of three set bits.

# Example 2:
# Input: n = 128
# Output: 1
# Explanation:
# The input binary string 10000000 has a total of one set bit.

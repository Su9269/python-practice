# Reverse bits of a given 32 bits signed integer.
# sol 1
class Solution(object):
    def reverseBits(self, n):
        final = []
        for i in range(1, 33):
            final.append(n & 1)
            n >>= 1
        binary_str = "".join(str(bit) for bit in final)
        return int(binary_str, 2)
# sol 2


class Solution(object):
    def reverseBits(self, n):
        ans = 0
        for i in range(1, 33):
            ans <<= 1
            ans += n & 1
            n >>= 1
        return ans

# Example 1:
# Input: n = 43261596
# Output: 964176192
# Explanation:
# Integer	Binary
# 43261596	00000010100101000001111010011100
# 964176192	00111001011110000010100101000000

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
# sol 1
class Solution(object):
    def singleNumber(self, nums):
        final = [x for x in nums if nums.count(x) == 1]
        return final[0]

# sol 2


class Solution(object):
    def singleNumber(self, nums):
        final = 0
        for num in nums:
            final ^= num
        return final
# 這個做法的核心是利用二進位的XOR(互斥或，符號為 ^)運算。
# XOR的規則很簡單：「相同得 0，不同得 1」。
# 這衍生出三個數學特性：
# 1.自己 XOR 自己會抵消：(A^A = 0)
# 2.任何數 XOR 0 都保持不變：(A^0 = A)
# 3.順序不重要(交換律)：(A^B^A = A^A^B = 0^B = B)


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

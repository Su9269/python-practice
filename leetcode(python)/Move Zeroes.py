# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# solution 1:
class Solution(object):
    def moveZeroes(self, nums):
        final = []
        for i in nums:
            if i != 0:
                final.append(i)
        b = len(nums)-len(final)
        for k in range(b):
            final.append(0)
        nums[:] = final


# solution 2:
class Solution(object):
    def moveZeroes(self, nums):
        # 1. 建立一個指標，紀錄「下一個非 0 元素」應該要擺放的位置
        insert_pos = 0

        # 2. 遍歷整個陣列
        for i in range(len(nums)):
            # 如果目前遇到的數字不是 0
            if nums[i] != 0:
                # 把這個非 0 數字，跟 insert_pos 位置的數字做交換
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                # 交換後，下一個非 0 數字該放的位置往後移一格
                insert_pos += 1

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

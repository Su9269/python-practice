# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# solution 1
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
        return i+1

# solution 2


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

# 核心邏輯：
# 1. 設定left, right兩個指標，代表目前的搜尋範圍（一開始涵蓋整個陣列）
# 2. 每輪迴圈計算中間點mid，比較nums[mid]跟target
# 3. 相等 → 直接回傳mid
# 4. nums[mid] > target → target在左半邊，right = mid - 1（排除mid本身，因為已確認不是答案）
# 5. nums[mid] < target → target在右半邊，left = mid + 1
# 6. 迴圈結束條件：left > right（範圍搜尋完畢，代表target不存在）
# 7. 跑完迴圈都沒找到 → return left，這個位置剛好就是target該插入的位置

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

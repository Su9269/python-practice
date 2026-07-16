# 7.Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        # 類型：快慢指標(Fast & Slow Pointers)
        # 觸發關鍵字：已排序陣列 + in-place + 去重複

        if len(nums) == 0:
            return 0

        slow = 0
        # slow：慢指標，代表「目前不重複區域，最後一個確定位置的索引」
        # nums[0] 自己一定是獨一無二的，所以 slow 從 0 開始

        for i in range(1, len(nums)):
            # i：快指標，一路往前逐一檢查每個數字

            if nums[i] != nums[slow]:
                # 因為陣列已排序，重複數字一定緊挨在一起
                # 只要 nums[i] 跟「不重複區域最後一個值」不同，代表找到新數字

                slow += 1
                # 先把「不重複區域」邊界往後擴大一格，空出新位置

                nums[slow] = nums[i]
                # 把新數字搬到剛空出來的位置，覆蓋掉原本重複的舊值

        return len(set(nums))
        # slow 是「最後一個不重複元素的索引」(從0算起)
        # 索引+1 才是「數量」，例如 slow=2 代表索引0,1,2共3個，要+1才是k

        # 易犯錯的坑：
        # 1. range(len(nums)) 會導致 nums[i+1] 存取超出範圍(IndexError)
        #    改用 for i in range(1, len(nums))，比較「當前」與「slow位置」，不比較i+1
        # 2. .sort() 是原地排序，回傳值是 None，不能寫成 nums = nums.sort()
        # 3. 下次遇到類似題型可聯想：Merge Two Sorted Lists（雙指標概念相通）

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

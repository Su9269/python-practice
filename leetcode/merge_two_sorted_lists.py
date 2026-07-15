# 6.Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        return dummy.next
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# 類型：Linked List（鏈結串列）+ 雙指標（Two Pointers）合併
# 觸發關鍵字：兩個（或多個）已排序的序列/串列，要合併成一個仍然排序的結果
# 核心觀念(第一次遇到 Linked List 要先搞懂)：
# 鏈結串列不是 Python 的 list，不能直接用for遍歷
# 每個節點只有 .val（值）和 .next（指向下一個節點）
# 走訪要用while node is not None:搭配 node = node.next手動一步步移動

# 核心邏輯：
# 1. 建一個 dummy（假）起始節點，用來當作新串列的起點，最後回傳時用dummy.next（跳過假節點）
# 2. current指標代表「新串列目前接到哪」，一開始指向 dummy
# 3. 只要兩邊都還有節點，就比較list1.val和list2.val，小的那個接上去，那個串列的指標往後移一格
# 4. 關鍵易錯點：current = current.next這行要放在 if/else 外面，每輪都要執行，不然新串列的指標不會往前移動，後面接的東西會蓋掉前面接的
# 5. 迴圈結束後，兩邊一定有一個變成None，另一個可能還有剩，判斷哪個還有剩，直接整串接上去（不用再逐一處理，因為那串本身已經排好序）

# 易犯的錯（自己踩過的坑）：
# Python 沒有大括號分區塊，完全靠縮排判斷程式碼層級，縮排錯一格不會報錯，但邏輯會完全跑掉且不容易發現
# 誤以為輸入是普通list，其實是ListNode物件（鏈結串列頭）

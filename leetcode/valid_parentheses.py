# 5.Valid Parentheses
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                if stack == [] or mapping[char] != stack[-1]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        return stack == []
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# 類型：Stack 應用
# 觸發關鍵字：括號配對、巢狀結構、"最後放進去的最先被處理"
# 核心邏輯：
# 1.左括號 → push進stack
# 2.右括號 → 檢查兩件事：
# stack 是不是空的（沒有左括號可以配對，直接 invalid）
# stack 最上層的左括號，跟這個右括號對不對得起來（用字典查表比對）
# 3.比對成功 → pop 掉，代表這組括號已完成配對
# 4.字串跑完 → 檢查stack是不是空的，不是空的代表還有左括號沒被關閉

# 易犯的錯(自己踩過的坑)：
# and/or條件順序錯，導致對空 stack 做 stack[-1] 直接報錯 → 要把「安全性檢查」放在條件最前面，靠短路機制擋掉危險操作
# 比對成功後忘記 pop，導致 stack 一直累積，最後判斷錯誤
# 忘記在最後檢查 stack 是否清空，只用return True寫死，漏掉「只有左括號、沒有右括號」這種情況

# 字典設計技巧：
# 只把右括號放進字典當 key，因為只有遇到右括號時才需要「查表比對」；左括號不需要查表，只需要 push，所以不用放進字典。char in mapping這句話因此天然等同於「這是右括號嗎」？

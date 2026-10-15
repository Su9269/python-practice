# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.
import random

# 1. 在全域（或類別外）定義秘密數字
# 你可以手動指定，例如 SECRET_NUMBER = 6
# 這裡用隨機產生 1 到 100 之間的數字
SECRET_NUMBER = random.randint(1, 100)


def guess(num):
    """
    LeetCode 系統模擬函式
    @param num: 你猜的數字
    @return: -1 如果你猜得太高
             1 如果你猜得太低
             0 如果你猜對了
    """
    if num > SECRET_NUMBER:
        return -1
    elif num < SECRET_NUMBER:
        return 1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n
        if n == 1:
            return 1
        while left <= right:
            mid = (left+right)//2
            ans = guess(mid)
            if ans == 0:
                return mid
            elif ans == -1:
                right = mid-1
            elif ans == 1:
                left = mid+1

# Example 1:
# Input: n = 10, pick = 6
# Output: 6

# Example 2:
# Input: n = 1, pick = 1
# Output: 1

# Example 3:
# Input: n = 2, pick = 1
# Output: 1

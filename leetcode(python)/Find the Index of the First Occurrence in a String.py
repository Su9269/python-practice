# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

# 1(第一種作法)
class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# 2(第二種作法)


class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1
# 因為range()本身「不包含結尾的那個數字」，如果你要i真正跑到len(haystack)-len(needle)這個位置（也就是最後一個有效的起始點），你必須讓range產生的範圍多涵蓋一個，所以要+1。
# haystack[i:i+len(needle)]這個切出來的片段,剛好等於needle

# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

# solution 1
class Solution(object):
    def wordPattern(self, pattern, s):
        final_pattern = list(pattern)
        final_s = s.split()
        if len(final_pattern) != len(final_s):
            return False
        box = {}
        for i in range(len(final_pattern)):
            if final_pattern[i] not in box:
                if final_s[i] in box.values():
                    return False
                box[final_pattern[i]] = final_s[i]
        my_pattern = [box[key] for key in final_pattern]
        return my_pattern == final_s

# solution 2


class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        # 長度要一樣，且字母種類數、單字種類數、以及他們配對後的種類數都要一樣
        # zip 像拉鍊一樣會把兩兩元素綁在一起
        return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))


# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

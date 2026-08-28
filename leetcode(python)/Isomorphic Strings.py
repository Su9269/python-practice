# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

# solution 1
class Solution(object):
    def isIsomorphic(self, s, t):
        s_pattern = []
        t_pattern = []
        for char in s:
            s_pattern.append(s.find(char))
        for char in t:
            t_pattern.append(t.find(char))
        return s_pattern == t_pattern


# solution2:
class Solution(object):
    def isIsomorphic(self, s, t):
        s_pattern = {}
        t_pattern = {}
        for char_s, char_t in zip(s, t):
            if char_s in s_pattern:
                if s_pattern[char_s] != char_t:
                    return False
            else:
                s_pattern[char_s] = char_t
            if char_t in t_pattern:
                if t_pattern[char_t] != char_s:
                    return False
            else:
                t_pattern[char_t] = char_s
        return True


# Example 1:
# Input: s = "egg", t = "add"
# Output: true
# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

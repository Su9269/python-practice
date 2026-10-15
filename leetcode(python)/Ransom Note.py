# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# sol 1
import collections as Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for word in ransomNote:
            if word in magazine:
                magazine = magazine.replace(word, "", 1)
            else:
                return False
        return True

# sol 2


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        for word, count in r_count.items():
            if m_count[word] < count:
                return False
        return True
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false

# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false

# 4.Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(x)for x in strs)
        ans = ""
        for i in range(min_len):
            letter = strs[0][i]
            for word in strs[1:]:
                if word[i] != letter:
                    return ans
            ans += letter
        return ans


# Input: strs = ["flower","flow","flight"]
# Output: "fl"
sol = Solution()
result = sol.longestCommonPrefix(["flower", "flow", "flight"])
print(repr(result))

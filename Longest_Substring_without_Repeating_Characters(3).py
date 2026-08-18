class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return len(s)

        seen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res,r - l + 1)

        return res
        
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = strs[0]

        for i in strs:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
            
        return prefix

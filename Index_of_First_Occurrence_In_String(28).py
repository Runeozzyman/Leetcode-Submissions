class Solution(object):
    def strStr(self, haystack, needle):
        
        if len(needle) > len(haystack):
            return -1
        elif needle == haystack:
            return 0

        for i in range(len(haystack)-len(needle)+1):
            if(haystack[i:len(needle)+i] == needle):
                return i
        return -1
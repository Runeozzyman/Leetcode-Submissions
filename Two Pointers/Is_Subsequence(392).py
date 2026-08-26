class Solution(object):
    def isSubsequence(self, s, t):
        
        if (len(s) > len(t)): return False
        elif (len(s) == 0): return True

        count = 0

        for i in range(0,len(t)):
            if(count == len(s)):
                return True
            elif (s[count] == t[i]):
                count += 1
            
        return count == len(s)
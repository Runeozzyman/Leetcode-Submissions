class Solution(object):
    def isIsomorphic(self, s, t):
        
        if len(s) != len(t):
            return False

        sChars = []
        tChars = []

        for char in s:            
            sChars.append(s.index(char))
        
        for char in t:
            tChars.append(t.index(char))

        if sChars == tChars:
            return True

        return False
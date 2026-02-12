class Solution(object):
    def wordPattern(self, pattern, s):
        
        patternMap = []
        stringMap = []

        splitString = s.split()

        for char in pattern:
            patternMap.append(pattern.index(char))
        
        for string in splitString:
            stringMap.append(splitString.index(string))
        
        if patternMap == stringMap:
            return True
        
        return False
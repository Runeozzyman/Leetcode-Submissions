class Solution(object):
    def lengthOfLastWord(self, s):

        stripped = s.strip().split()

        if len(s) == 0:
            return 0
    
        lastWord = stripped[len(stripped)-1]

        return len(lastWord)
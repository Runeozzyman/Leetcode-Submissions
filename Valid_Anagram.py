class Solution(object):
    def isAnagram(self, s, t):
        
        letters1 = {}
        letters2 = {}

        for letter in s:
            letters1[letter] = letters1.get(letter,0)+1
        for letter in t:
            letters2[letter] = letters2.get(letter,0)+1

        if letters1 == letters2:
            return True

        return False
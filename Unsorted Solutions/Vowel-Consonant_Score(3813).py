class Solution(object):
    def vowelConsonantScore(self, s):
        
        vowels = ['a','e','i','o','u']
        v = c = 0

        for char in s:
            
            if char.isalpha():
                if char in vowels:
                    v += 1
                
                else:
                    c += 1
            
        if (c == 0):
            return 0
        
        return int(floor(v/c))
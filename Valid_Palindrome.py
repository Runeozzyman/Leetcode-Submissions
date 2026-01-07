class Solution(object):
    def isPalindrome(self, s):

        result = ""
        
        for char in s:
            if char.isalnum():
                result += char.lower()
            else: 
                continue

        return result[::-1] == result
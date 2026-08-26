class Solution(object):
    def isPalindrome(self, x):
        xString = str(x)
        palindrome = xString[::-1]

        if xString == palindrome :
            return True

        return False
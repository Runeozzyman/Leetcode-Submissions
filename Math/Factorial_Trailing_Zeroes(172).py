class Solution(object):
    def trailingZeroes(self, n):
        
        zeroes = 0

        while n>0:
            n /= 5
            zeroes += n
        
        return zeroes
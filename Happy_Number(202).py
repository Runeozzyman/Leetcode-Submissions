class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            res = 0
            while n > 0:
                rem = n % 10
                res += rem * rem
                n //= 10
            n = res
            
        return True
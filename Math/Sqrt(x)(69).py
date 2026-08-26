class Solution(object):
    def mySqrt(self, x):
        #idea is to use binary search for logarithmic time

        left = 1
        right = x

        if x==0:
            return 0

        while left <= right:
            mid = (left+right)//2

            if mid*mid == x:
                return mid
            
            elif mid*mid > x:
                right = mid-1

            else:
                left=mid+1
            
        return right






        
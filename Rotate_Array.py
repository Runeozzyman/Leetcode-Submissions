class Solution(object):      

    def rotate(self, nums, k):

        n = len(nums)
        result = [0]*n
        k = k%n

        for i in range(n):
            result[(i+k)%n] = nums[i]
        for i in range(n):
            nums[i] = result[i]
        
        return nums
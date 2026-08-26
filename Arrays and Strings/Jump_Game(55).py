class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target = len(nums) - 1 #last index of array
        
        #start at 2nd last element, backtrack through array
        for i in range(len(nums)-2, -1, -1):
            #if 
            if nums[i] + i >= target:
                target = i
            
        return target == 0
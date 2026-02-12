class Solution(object):
    def longestConsecutive(self, nums):
        
        nums.sort()

        longest = 1
        maxLength = 1

        if not nums:
            return 0

        for i in range(len(nums)-1):

            if(nums[i] == nums[i+1]):
                continue

            if(nums[i]+1 == nums[i+1]):
                longest += 1

            else: 
                longest = 1

            maxLength = max(maxLength, longest)
        
        return maxLength
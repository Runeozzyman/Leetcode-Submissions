class Solution(object):
    def missingMultiple(self, nums, k):
        
        smallest = k

        for i in range(len(nums)):
            if smallest not in nums:
                return smallest
            smallest = k*(i+2)
        
        return smallest
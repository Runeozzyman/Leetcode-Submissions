class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        
        seen = {}

        for index, val in enumerate(nums):
            if val in seen and index - seen[val] <= k:
                return True
            seen[val] = index
        return False
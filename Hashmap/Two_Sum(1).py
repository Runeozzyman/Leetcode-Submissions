class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i in range(len(nums)):
            complement = target-nums[i]
            if complement in seen:
                return [i, seen[complement]]
            seen[nums[i]] = i
        
        return []
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        ans = [0] * len(nums) 

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1

        for j in range(len(nums)-1, -1, -1):
            ans[j] *= suffix
            suffix *= nums[j]
        
        return ans
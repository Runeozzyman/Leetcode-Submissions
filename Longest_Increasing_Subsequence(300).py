class Solution(object):
    def lengthOfLIS(self, nums):
        sub = []

        for num in nums:
            if len(sub) == 0 or sub[-1] < num:
                sub.append(num)
            else:
                idx = bisect_left(sub,num)
                sub[idx] = num
            
        return len(sub)
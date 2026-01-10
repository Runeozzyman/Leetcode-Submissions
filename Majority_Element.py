class Solution(object):
    def majorityElement(self, nums):
        
        numDict = {}
        majority = int(len(nums)/2)

        for num in nums:
            numDict[num] = numDict.get(num,0)+1
        for key,val in numDict.items():
            if (val > majority):
                return key
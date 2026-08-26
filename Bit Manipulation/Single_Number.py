class Solution(object):
    def singleNumber(self, nums):
        
        numDict = {}
        for num in nums:
            numDict[num] = numDict.get(num,0)+1
        for key, val in numDict.items():
            if val == 1:
                return key

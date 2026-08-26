class Solution(object):
    def twoSum(self, numbers, target):

        dic = {}

        for i,v in enumerate(numbers):
            if target-v in dic:
                return[dic[target-v]+1,i+1]
            dic[v] = i
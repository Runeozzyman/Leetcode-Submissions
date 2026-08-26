class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        curr_tank = start = 0
        
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):

            curr_tank += gas[i] - cost[i]

            if curr_tank<0:
                start = i+1
                curr_tank = 0
            
        return start

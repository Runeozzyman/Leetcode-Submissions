class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        maxProfit = 0


        while(sell < len(prices)):
            currentProfit = prices[sell] - prices[buy]
            if(currentProfit > maxProfit):
                maxProfit = currentProfit
            elif(prices[buy] > prices[sell]):
                buy = sell
                sell += 1
            else: sell += 1
        
        return maxProfit
            
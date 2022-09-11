class Solution(object):
    def maxProfit(self, prices):
        
        buy = prices[0]
        profit =0
        for i in range (1,len(prices)):
            diff = prices[i]-buy
            buy = min(buy, prices[i])
            profit= max(profit,diff)
        return profit

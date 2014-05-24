class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):        
        profit = 0
        
        if not prices:
            return profit
            
        buy = prices[0]
        
        for i in range(1,len(prices)):
            profit = max(prices[i]-buy, profit)
            buy = min(buy, prices[i])
        
        return profit
class Solution(object):
    def maxProfit(self, prices):
        k=0
        n=1
        profit=0
        while n < len(prices):
          if prices[n] - prices[k] > profit:
            profit = prices[n] - prices[k]
          if prices[n] < prices[k]:
            k = n
          n=n+1  
        return profit

            
            
        
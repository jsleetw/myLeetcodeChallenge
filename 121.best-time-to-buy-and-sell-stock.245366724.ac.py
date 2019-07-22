class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #time: O(n)
        #space: O(1)
        
        #init
        max_profit = 0
        min_price = float("inf")
        
        #only find min_price and max_profit
        for i in range(len(prices)):
            if (prices[i] < min_price):
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            
            #print(min_price, max_profit)
        return max_profit
        

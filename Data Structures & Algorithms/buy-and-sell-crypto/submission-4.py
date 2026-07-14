class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = prices[0]
        maxProfit = 0

        for price in prices:
            maxProfit = max(maxProfit, price - l)
            if price < l:
                l = price
        
        return maxProfit
            

        
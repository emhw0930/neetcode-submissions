class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        max_profit = 0

        for r in prices:
            if r < l:
                l = r
            if r - l > max_profit:
                max_profit = r - l
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]

        for price in prices:
            mini = min(price, mini)
            res = max(price - mini, res)
        
        return res

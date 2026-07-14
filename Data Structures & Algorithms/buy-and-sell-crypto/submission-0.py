class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        mini = prices[0]

        for price in prices:
            if price < mini:
                mini = price
            max_diff = max(price - mini, max_diff)

        return max_diff
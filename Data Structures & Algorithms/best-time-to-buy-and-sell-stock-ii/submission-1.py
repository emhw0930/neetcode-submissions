class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        result = 0
        for r in prices:
            if r > l:
                result += r - l
            l = r
        return result
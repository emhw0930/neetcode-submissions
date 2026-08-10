class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] = number of ways to reach ith amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                start = i - coin
                if start < 0:
                    continue
                dp[i] = min(dp[start] + 1, dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1
        
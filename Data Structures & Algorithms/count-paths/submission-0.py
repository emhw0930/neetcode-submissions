class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # two directions: right, down
        # every time you can have right and down 
        # so make a dp where we add up and left value
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row - 1 >= 0 :
                    dp[row][col] += dp[row - 1][col]
                if col - 1 >= 0:
                    dp[row][col] += dp[row][col - 1]
        return dp[m - 1][n - 1]

        
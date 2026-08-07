class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[10001] * (i + 1) for i in range(len(triangle))]
        for i in range(len(triangle)):
            for j in range(i + 1):
                # get for each [i][j] get the min(dp[i - 1][j], dp[i - 1][j - 1])
                if i == 0:
                    dp[i][j] = triangle[i][j]
                else:
                    if 0 < j < i:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]
                    else:
                        if j == 0:
                            dp[i][j] = dp[i - 1][j] + triangle[i][j]
                        else:
                            dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]
        return min(dp[len(triangle) - 1])

        
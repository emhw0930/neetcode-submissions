class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = [0] * len(points[0])
        for row in range(len(points)):
            curr = []
            for col in range(len(points[0])):
                maxi = 0
                for i in range(len(dp)):
                    maxi = max(maxi, dp[i] + points[row][col] - abs(i - col))
                curr.append(maxi)
            dp = curr
        return max(dp)
        
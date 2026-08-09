class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i, num in enumerate(nums):
            end = min(len(nums), i + num + 1)
            if dp[i]:
                for j in range(i, end):
                    dp[j] = True
                    if dp[-1] == True:
                        return True
        return dp[-1]

        
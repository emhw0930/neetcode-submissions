class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(len(nums)):
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]
        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def dfs(curr, remain):
            if len(curr) == n:
                result.append(curr)
                return
            for i in range(len(remain)):
                dfs(curr + [remain[i]], remain[:i] + remain[i + 1:])
        dfs([], nums)
        return result
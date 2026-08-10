class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        def dfs(curr, remain):
            if len(curr) == len(nums):
                visited.add(tuple(curr))
                return
            for i in range(len(remain)):
                dfs(curr + [remain[i]], remain[:i] + remain[i + 1:])
        dfs([], nums)
        return list(visited)
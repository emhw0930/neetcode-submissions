class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(curr, i):
            if len(curr) == k:
                result.append(curr[:])
            for j in range(i, n + 1):
                curr.append(j)
                dfs(curr, j + 1)
                curr.pop()
        dfs([], 1)
        return result

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        visited.add(tuple([]))
        result = [[]]

        def dfs(j, curr):
            if tuple(sorted(curr)) not in visited:
                result.append(curr.copy())
                visited.add(tuple(sorted(curr.copy())))
            for i in range(j, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        
        dfs(0, [])

        return result


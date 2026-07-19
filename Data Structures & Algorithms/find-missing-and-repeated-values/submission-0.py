class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        visited = set()
        result = [-1, -1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in visited:
                    result[0] = grid[i][j]
                visited.add(grid[i][j])
        result[1] = sum(range(1, len(grid) ** 2 + 1)) - sum(visited)
        return result
        
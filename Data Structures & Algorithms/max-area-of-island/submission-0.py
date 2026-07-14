class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or (row, col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(dfs(row, col), max_area)
        
        return max_area
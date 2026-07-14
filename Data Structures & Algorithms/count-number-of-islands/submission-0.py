class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        num_island = 0

        def dfs(row, col):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    num_island += 1
                    dfs(r, c)
        
        return num_island
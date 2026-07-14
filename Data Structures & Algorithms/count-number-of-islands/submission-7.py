class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or (row, col) in visited or grid[row][col] == "0":
                return
            visited.add((row, col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        res = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and (row, col) not in visited: 
                    res += 1
                    dfs(row, col)

        return res

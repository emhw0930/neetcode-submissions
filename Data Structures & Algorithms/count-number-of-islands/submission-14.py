class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def dfs(row, col):
            if row < 0 or col >= COL or col < 0 or row >= ROW or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            for x, y in directions:
                nr, nc = row + x, col + y
                dfs(nr, nc)
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r, c)
        return count
    
                    

        

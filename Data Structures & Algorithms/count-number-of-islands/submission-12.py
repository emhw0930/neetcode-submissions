class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visited = set()
        def dfs(row, col):
            if row < 0 or col >= COL or col < 0 or row >= ROW or (row, col) in visited or grid[row][col] == "0":
                return
            visited.add((row, col))
            for x, y in directions:
                nr, nc = row + x, col + y
                dfs(nr, nc)
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        return count
    
                    

        

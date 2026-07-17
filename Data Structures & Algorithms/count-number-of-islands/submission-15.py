class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                row, col = queue.popleft()
                for dx, dy in directions:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
        count = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    count += 1
                    bfs(r, c)
        return count
    
                    

        

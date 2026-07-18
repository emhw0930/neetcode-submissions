class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row, col):
            queue = deque([[row, col]])
            grid[row][col] = 0
            area = 1
            while queue:
                row, col = queue.popleft()
                for dx, dy in directions:
                    nr, nc = row + dx, col + dy
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:
                        queue.append([nr, nc])
                        grid[nr][nc] = 0
                        area += 1
            return area
        
        max_area = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        print(grid)

        return max_area
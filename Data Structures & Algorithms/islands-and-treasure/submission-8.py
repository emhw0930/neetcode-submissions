class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        INF = 2147483647

        def bfs(row, col):
            queue = deque()
            visited = set()
            queue.append((row, col, 0))
            visited.add((row, col))
            while queue:
                row, col, step = queue.popleft()
                if grid[row][col] == 0:
                    return step
                for row_diff, col_diff in directions:
                    new_row = row + row_diff
                    new_col = col + col_diff
                    if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL or grid[new_row][new_col] == -1 or (new_row, new_col) in visited:
                        continue
                    queue.append((new_row, new_col, step + 1))
                    visited.add((new_row, new_col))
            return INF
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == INF:
                    grid[row][col] = bfs(row, col)
        
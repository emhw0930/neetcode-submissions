class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row, col):
            area = 0
            queue = deque()
            queue.append((row, col))
            visited.add((row, col))
            while queue:
                row, col = queue.popleft()
                area += 1
                for direction in directions:
                    row_diff, col_diff = direction
                    new_row = row + row_diff
                    new_col = col + col_diff
                    if new_row < 0 or new_col < 0 or new_row >= ROW or new_col >= COL or (new_row, new_col) in visited or grid[new_row][new_col] == 0:
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            return area

        max_area = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1 and (row, col) not in visited:
                    area = bfs(row, col)
                    max_area = max(area, max_area)

        return max_area
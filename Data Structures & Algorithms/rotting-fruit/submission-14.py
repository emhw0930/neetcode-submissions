class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row, col):
            queue = deque()
            visited = set()
            queue.append((row, col, 0))
            visited.add((row, col))
            max_step = 0
            while queue:
                r , c, step = queue.popleft()
                visited.add((r, c))
                for row_dic, col_dic in directions:
                    new_r = r + row_dic
                    new_c = c + col_dic
                    if new_r < 0 or new_c < 0 or new_r >= ROW or new_c >= COL or (new_r, new_c) in visited or grid[new_r][new_c] == 0:
                        continue
                    queue.append((new_r, new_c, step + 1))
                if grid[r][c] == 2:
                    return step
            return -1

        res = 0
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    if bfs(row, col) == -1:
                        return -1
                    res = max(res, bfs(row, col))
        
        return res
                

        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        dire = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def bfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or (row, col) in visited or grid[row][col] == "0":
                return
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                for rd, cd in dire:
                    nr, nc = row + rd, col + cd
                    if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue
                    visited.add((nr, nc))
                    queue.append((nr, nc))
        
        res = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and (row, col) not in visited: 
                    res += 1
                    bfs(row, col)

        return res

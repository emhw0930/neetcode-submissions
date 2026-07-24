class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visited_dfs = set()
        min_dist = float("inf")

        def bfs(lst):
            queue = deque(lst)
            visited = set(lst)
            step = 0
            nonlocal min_dist
            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if 0 <= nr < ROW and 0 <= nc < COL and (nr, nc) not in visited:
                            visited.add((nr, nc))
                            if grid[nr][nc] == 1:
                                min_dist = min(min_dist, step)
                                return 
                            else:
                                queue.append((nr, nc))
                step += 1
        
        def dfs(row, col, lst):
            if row < 0 or row >= ROW or col < 0 or col >= COL or grid[row][col] != 1 or (row, col) in visited_dfs:
                return
            visited_dfs.add((row, col))
            lst.append((row, col))
            for dr, dc in directions:
                dfs(row + dr, col + dc, lst)
        
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1 and (row, col) not in visited_dfs:
                    lst = []
                    dfs(row, col, lst)
                    bfs(lst)
        
        return min_dist

        
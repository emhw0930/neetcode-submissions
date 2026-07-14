class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        queue = deque()

        def bfs(row, col):
            if row < 0 or col < 0 or row >= ROW or col >= COL or (row, col) in visited or grid[row][col] == "0":
                return
            visited.add((row, col))
            queue.append((row + 1, col))
            queue.append((row - 1, col))
            queue.append((row, col + 1))
            queue.append((row, col - 1))
            while queue:
                nex = queue.popleft()
                bfs(nex[0], nex[1])
        
        res = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == "1" and (row, col) not in visited: 
                    res += 1
                    bfs(row, col)

        return res

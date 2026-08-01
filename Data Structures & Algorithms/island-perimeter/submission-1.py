class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # so for every block, add up the # of sides that are not connected to another island block
        self.visited = set()
        self.count = 0
        self.direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in self.visited or grid[row][col] == 0:
                return
            neighbor_count = 0
            self.visited.add((row, col))
            for dr, dc in self.direction:
                nr, nc = row + dr, col + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    neighbor_count += 1
                dfs(nr, nc)
            side = 4 - neighbor_count
            self.count += side
                
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return self.count

        
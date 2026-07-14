class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        ROW = len(grid)
        COL = len(grid[0])
        visited = set()
        queue = deque() # que in python

        def add(r, c):
            if (
                r < 0 or
                r >= ROW or
                c < 0 or
                c >= COL or
                (r, c) in visited or
                grid[r][c] == -1
            ): 
                return
            visited.add((r, c))
            queue.append([r, c])

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append([r, c])

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1

        



        
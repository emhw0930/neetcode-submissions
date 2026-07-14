class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        visited = set()

        def add(r, c):
            if (
                r < 0 or
                c < 0 or
                r >= ROW or
                c >= COL or
                grid[r][c] == -1 or
                (r, c) in visited
            ):
                return 
            visited.add((r, c))
            queue.append([r, c])
        
        # add all the treasure chest position into queue so they can start simotaneously 
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append([r,c])

        dist = 0
        # implement bfs
        while queue: # while queue have stuff
            for i in range(len(queue)):
                r, c = queue.popleft() # pop the first item added
                grid[r][c] = dist
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            dist += 1


        



        
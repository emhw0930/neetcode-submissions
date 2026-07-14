class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        queue = deque()
        visited = set()
        fresh = []

        def add(r, c):
            if (
                r < 0 or
                c < 0 or
                r >= ROW or
                c >= COL or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return
            fresh.pop()
            visited.add((r, c))
            queue.append([r, c])

        # add initial rotten fruit into visited and queue
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh.append(1)

        # BFS
        length = 0
        while len(fresh) > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            length += 1
        
        return length if len(fresh) == 0 else -1



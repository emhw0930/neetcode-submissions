class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        self.graph = defaultdict(list)
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.heights = [0] * n
        for i in range(n):
            self.visited = {i}
            self.dfs(i, i, 0)
        min_h = min(self.heights)
        return [i for i in range(n) if self.heights[i] == min_h]

    def dfs(self, i, node, height):
        self.heights[i] = max(height, self.heights[i])
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.visited.add(neighbor)
                self.dfs(i, neighbor, height + 1)
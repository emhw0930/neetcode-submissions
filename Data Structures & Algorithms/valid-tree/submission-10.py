class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:      # tree must have exactly n-1 edges
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)          # both directions

        visited = set()
        self.result = True
        def dfs(node, parent):
            visited.add(node)
            for nex in adj[node]:
                if nex == parent:     # skip the edge we arrived on
                    continue
                if nex in visited:    # already seen via another path → cycle
                    return False
                if not dfs(nex, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n
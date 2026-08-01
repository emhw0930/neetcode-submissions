class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        stack = [0]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            for nex in adj[node]:
                if nex not in visited:
                    stack.append(nex)
        return len(visited) == n
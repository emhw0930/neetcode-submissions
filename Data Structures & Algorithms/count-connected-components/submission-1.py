class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        mapi = defaultdict(list)
        for i in range(n):
            mapi[i] = []
        for u, v in edges:
            mapi[u].append(v)
            mapi[v].append(u)
        visited = set()
        def dfs(node):
            visited.add(node)
            for nex in mapi[node]:
                if nex in visited:
                    continue
                dfs(nex)
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count

        
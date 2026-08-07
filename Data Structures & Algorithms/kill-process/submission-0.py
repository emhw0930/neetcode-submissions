class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = defaultdict(list)
        for child, parent in zip(pid, ppid):
            graph[parent].append(child)
        killed = []
        def dfs(node):
            killed.append(node)
            children = graph[node]
            for child in children:
                dfs(child)
        dfs(kill)
        return killed

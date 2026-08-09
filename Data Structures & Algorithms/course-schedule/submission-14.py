class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(numCourses):
            graph[i] = []
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        course = [graph[i] == [] for i in range(numCourses)]
        visited = set()
        def dfs(node):
            result = [False] * len(graph[node])
            visited.add(node)
            for i, prereq in enumerate(graph[node]):
                if course[prereq]:
                    result[i] = True
                elif prereq not in visited:
                    result[i] = dfs(prereq)
            if result and all(result):
                course[node] = True
                return True
        for i in range(numCourses):
            dfs(i)
        return all(course)


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(numCourses):
            graph[i] = []
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        course = [graph[i] == [] for i in range(numCourses)]
        # print(graph)
        # print(course)
        visited = set()
        def dfs(node):
            result = []
            visited.add(node)
            for prereq in graph[node]:
                if course[prereq]:
                    result.append(True)
                elif prereq not in visited:
                    # print(prereq, dfs(prereq), result)
                    result.append(dfs(prereq))
                elif prereq in visited:
                    result.append(False)
            # print(node)
            # print(course)
            if result and all(result):
                course[node] = True
                return True
        for i in range(numCourses):
            dfs(i)
        return all(course)


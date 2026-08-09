class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # 0 = unvisited, 1 = visiting (on stack), 2 = done
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:      # back edge → cycle
                return False
            if state[node] == 2:      # already proven finishable
                return True
            state[node] = 1
            for prereq in graph[node]:
                if not dfs(prereq):
                    return False
            state[node] = 2
            return True

        return all(dfs(i) for i in range(numCourses))
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}

        # fill in the adjencent list
        for edge in prerequisites:
            course, prereq = edge
            adj[course].append(prereq)

        # DFS 
        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if adj[c] == []:
                return True
            visited.add(c)
            for prereq in adj[c]:
                if not dfs(prereq):
                    return False
            visited.remove(c)
            adj[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True



            
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        coursepre=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            coursepre[a].append(b)
        visited=set()
        def dfs(node):
            if node in visited:
                return False
            if len(coursepre[node])==0:
                return True
            visited.add(node)
            for c in coursepre[node]:
                if not dfs(c): return False
            visited.remove(node)
            coursepre[node]=[]
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            pre[a].append(b)
        visited=set()
        def dfs(node):
            if node in visited:
                #### loop 
                return False
            if len(pre[node])==0:
                return True
            visited.add(node)
            for c in pre[node]:
                if not dfs(c): return False
            visited.remove(node)
            pre[node]=[]
            return True
        for i in range(numCourses):
            if not dfs(i): return False
        return True

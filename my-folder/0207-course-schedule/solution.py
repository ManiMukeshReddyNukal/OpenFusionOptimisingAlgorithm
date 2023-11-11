class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        req={i:[] for i in range(numCourses)}
        s=set()
        for i,j in prerequisites:
            req[i].append(j)
        def dfs(node):
            if node in s:
                return False
            if len(req[node])==0:
                return True
            s.add(node)
            for c in req[node]:
                if not dfs(c):return False
            s.remove(node)
            req[node]=[]
            return True
        for i in range(numCourses):
            if not dfs(i):return False
        return True

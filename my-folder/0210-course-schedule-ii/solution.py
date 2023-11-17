class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        pre=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            pre[a].append(b)
        out=[]
        visit,cycle=set(),set()
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for c in pre[node]:
                if not dfs(c): return False
            cycle.remove(node)
            visit.add(node)
            out.append(node)
            return True
        for c in range(numCourses):
            if not dfs(c): return []
        return out

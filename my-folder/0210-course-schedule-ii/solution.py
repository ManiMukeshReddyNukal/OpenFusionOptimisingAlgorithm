class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap=[[] for _ in range(numCourses)]
        for a,b in prerequisites:
            premap[a].append(b)
        visit,cycle=set(),set()
        output=[]
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for a in premap[node]:
                if dfs(a)==False:
                    return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return output

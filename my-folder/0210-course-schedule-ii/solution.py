class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=collections.defaultdict(list)
        for (a,b) in prerequisites:
            graph[a].append(b)
        visited=set()
        cycle=set()
        out=[]
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for adjnode in graph[node]:
                if not dfs(adjnode):
                    return False
            cycle.remove(node)
            visited.add(node)
            out.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
        return out

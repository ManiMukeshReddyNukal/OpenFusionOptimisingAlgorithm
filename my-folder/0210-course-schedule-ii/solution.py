class Solution:
    def findOrder(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[1]].append(e[0])
        indeg = [0 for i in range(n)]
        for lst in adj:
            for node in lst:
                indeg[node] += 1
        q = deque()
        for i in range(n):
            if indeg[i]==0: q.append(i)
        order = []
        while q:
            curnode = q.popleft()
            order.append(curnode)
            for neigh in adj[curnode]:
                indeg[neigh]-=1
                if indeg[neigh]==0: q.append(neigh)
        return order if all(indeg[i]==0 for i in range(n)) else []

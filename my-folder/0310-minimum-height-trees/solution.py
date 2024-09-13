class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        graph=[[] for _ in range(n)]
        degree=[0]*n
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            degree[a]+=1
            degree[b]+=1
        resp=[]
        q=deque([i for i,v in enumerate(degree) if v==1])
        while q:
            resp.clear()
            for _ in range(len(q)):
                node=q.popleft()
                resp.append(node)
                for adjnode in graph[node]:
                    degree[adjnode]-=1
                    if degree[adjnode]==1:
                        q.append(adjnode)
        return resp


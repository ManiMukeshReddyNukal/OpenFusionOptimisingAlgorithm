class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph=collections.defaultdict(dict)
        for u,v,w in edges:
            graph[u][v]=w
            graph[v][u]=w
        pq=[(0,0)]
        dist={0:0}
        visited={}
        ans=0
        while pq:
            d,node=heapq.heappop(pq)
            if d>dist[node]:
                continue
            ans+=1
            for adjnode,weight in graph[node].items():
                v=min(weight,maxMoves-d)
                visited[(node,adjnode)]=v
                ud=d+weight+1
                if ud<dist.get(adjnode,maxMoves+1):
                    heapq.heappush(pq, (ud,adjnode))
                    dist[adjnode]=ud
        for u,v,w in edges:
            ans+=min(w,visited.get((u,v),0)+visited.get((v,u),0))
        return ans

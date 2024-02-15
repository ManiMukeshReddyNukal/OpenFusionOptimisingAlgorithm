class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        graph={}
        for i in range(n):
            graph[i]=[]
        for i in range(n):
            for j in range(n):
                if j!=i:
                    dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    graph[i].append((j,dist))
                    graph[j].append((i,dist))
        pq=[(0,0)]
        visited=set()
        cost=0
        while pq:
            d,node=heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            cost+=d
            for neighbor,distance in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(pq,(distance,neighbor))
        return cost if len(visited)==n else -1

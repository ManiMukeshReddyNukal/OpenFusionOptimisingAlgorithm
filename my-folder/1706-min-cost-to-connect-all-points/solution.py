class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ### prims 
        graph=defaultdict(defaultdict)
        m=len(points)
        for i in range(m):
            for j in range(i,m):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                graph[i][j]=dist
                graph[j][i]=dist
        minheap=[]
        heapq.heappush(minheap,(0,0))
        visited=set()
        mincost=0
        while minheap:
            distance,node=heapq.heappop(minheap)
            if node not in visited:
                mincost+=distance
                visited.add(node)
                for adjnode,distance in graph[node].items():
                    heapq.heappush(minheap, (distance,adjnode))
        if len(visited)==m:
            return mincost
        else:
            return -1

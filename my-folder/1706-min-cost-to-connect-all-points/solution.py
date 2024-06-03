class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def nested_dict():
            return defaultdict(nested_dict)
        graph=defaultdict(nested_dict)
        m=len(points)
        n=len(points[0])
        for i in range(m):
            for j in range(m):
                if i!=j:
                    dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                    graph[i][j]=dist
                    graph[j][i]=dist
        minheap=[]
        heapq.heappush(minheap, (0,0))
        mincost=0
        visited=set()
        while minheap:
            distance,node=heapq.heappop(minheap)
            if node not in visited:
                mincost+=distance
                visited.add(node)
                for adjnode,adjdist in graph[node].items():
                    heapq.heappush(minheap, (adjdist,adjnode))
        if len(visited)==m: 
            return mincost
        else:
            return -1



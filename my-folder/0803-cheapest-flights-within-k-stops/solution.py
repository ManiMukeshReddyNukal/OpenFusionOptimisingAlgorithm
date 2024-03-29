class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type k: int
        :rtype: int
        """
        dist=[float('inf')]*n
        dist[src]=0
        for i in range(k+1):
            temp=dist[:]
            for [src,dest,cost] in flights:
                if dist[src]!=float('inf'):
                    temp[dest]=min(temp[dest],dist[src]+cost)
            dist=temp
        return dist[dst] if dist[dst] != float('inf') else -1

import heapq

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
        graph={i:[] for i in range(n)}
        for [s,d,c] in flights:
            graph[s].append((d,c))
        pq=[(0,src,0)]
        visited=dict()
        while pq:
            cost,city,stops=heapq.heappop(pq)
            if city==dst:
                return cost
            if stops>k:
                continue
            if (city,stops) in visited and visited[(city,stops)]<=cost:
                continue;
            visited[(city,stops)]=cost
            for (dest,price) in graph[city]:
                updated_cost=cost+price
                heapq.heappush(pq,(updated_cost,dest,stops+1))
        return -1

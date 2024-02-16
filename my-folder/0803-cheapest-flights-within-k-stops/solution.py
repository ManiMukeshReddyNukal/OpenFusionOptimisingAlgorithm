import heapq

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        # Graph initialization
        graph = {i: [] for i in range(n)}
        for s, d, p in flights:
            graph[s].append((d, p))
        
        # Priority queue: (cost, current node, stops made)
        pq = [(0, src, 0)]
        
        # Visited dictionary to keep track of the least cost to a node with a given number of stops
        visited = dict()
        
        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            # If destination is reached, return the cost
            if node == dst:
                return cost
            
            # If stops are over K, do not proceed further
            if stops > K:
                continue
            
            # Avoid revisiting a node with the same or more number of stops at a higher or equal cost
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            visited[(node, stops)] = cost
            
            # Explore the next nodes
            for next_node, price in graph[node]:
                next_cost = cost + price
                heapq.heappush(pq, (next_cost, next_node, stops + 1))
        
        # If destination is not reachable within K stops, return -1
        return -1


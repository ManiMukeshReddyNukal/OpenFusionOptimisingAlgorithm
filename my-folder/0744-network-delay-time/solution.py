import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize the network graph
        network = {}
        for i in range(1, n + 1):
            network[i] = []
        for src, dest, time in times:
            network[src].append((dest, time))
        
        # Initialize priority queue and minimum time dictionary
        pq = []
        mintime = {}
        heapq.heappush(pq, (0, k))
        
        # Dijkstra's algorithm
        while pq:
            time, source = heapq.heappop(pq)
            if source not in mintime:
                mintime[source] = time
                for d, t in network[source]:
                    if d not in mintime:
                        heapq.heappush(pq, (time + t, d))
        
        # Check if all nodes received the signal
        if len(mintime) != n:
            return -1
        
        return max(mintime.values())


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for [a,b,c] in times:
            graph[a].append([c,b])
        minheap=[]
        heapq.heappush(minheap, (0,k))
        visited={}
        while minheap:
            time,node=heapq.heappop(minheap)
            if node in visited:
                continue
            visited[node]=time
            for [adjdistance,adjnode] in graph[node]:
                if adjnode not in visited:
                    heapq.heappush(minheap, (adjdistance+time,adjnode))
        return max(visited.values()) if len(visited)==n else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for src,dest,weight in times:
            graph[src].append([dest,weight])
        minheap=[[0,k]]
        mindist={}
        while minheap:
            distance,node=heapq.heappop(minheap)
            if node in mindist:
                continue
            mindist[node]=distance
            for adjnode,adjdist in graph[node]:
                if adjnode not in mindist:
                    heapq.heappush(minheap, ((adjdist+distance,adjnode)))
        return max(mindist.values()) if len(mindist)==n else -1

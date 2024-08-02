class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for [s,t,d] in times:
            graph[s].append([t,d])
        minheap=[(0,k)]
        mindist={}
        while minheap:
            distance,node=heapq.heappop(minheap)
            if node in mindist:
                continue
            mindist[node]=distance
            for adjnodes,adjdist in graph[node]:
                if adjnodes not in mindist:
                    heapq.heappush(minheap, (distance+adjdist,adjnodes))
        return max(mindist.values()) if len(mindist)==n else -1

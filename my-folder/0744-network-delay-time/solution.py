class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph={}
        for i in range(1,n+1):
            graph[i]=[]
        for src,dest,weight in times:
            graph[src].append([weight,dest])
        pq=[]
        heapq.heappush(pq,(0,k))
        mintime={}
        while pq:
            time,dest=heapq.heappop(pq)
            if dest not in mintime:
                mintime[dest]=time
                for [t,adjn] in graph[dest]:
                    if adjn not in mintime:
                        heapq.heappush(pq,(t+time,adjn))
        if len(mintime)!=n:
            return -1
        return max(mintime.values())

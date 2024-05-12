class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        wtoq=[(w/q,q) for index,(w,q) in enumerate(zip(wage,quality))]
        wtoq.sort(key=lambda x:x[0])
        maxheap=[]
        current_quality=0
        totolcost=math.inf
        for i in range(len(quality)):
            heapq.heappush(maxheap, -wtoq[i][1])
            current_quality+=wtoq[i][1]
            if len(maxheap)>k:
                current_quality+=heapq.heappop(maxheap)
            if len(maxheap)==k:
                totolcost=min(totolcost,current_quality*wtoq[i][0])
        return totolcost

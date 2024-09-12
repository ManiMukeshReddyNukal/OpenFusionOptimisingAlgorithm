class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pq=[]
        for p,c in zip(profits,capital):
            heapq.heappush(pq, (-p,c))
        i=0
        arr=[]
        while i<k and pq:
            while pq:
                (p,c)=heapq.heappop(pq)
                if c<=w:
                    i+=1
                    w+=-p
                    break
                elif not pq:
                    return w
                else:
                    arr.append((p,c))
            while arr:
                heapq.heappush(pq, arr.pop())
        return w

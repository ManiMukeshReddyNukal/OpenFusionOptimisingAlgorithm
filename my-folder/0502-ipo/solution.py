class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hp=[]
        for p,c in zip(profits,capital):
            heapq.heappush(hp, (-p,c))
        i=0
        arr=[]
        while i<k and hp:
            while hp:
                (p,c)=heapq.heappop(hp)
                if c<=w:
                    w+=-p
                    i+=1
                    break
                elif not hp:
                    return w
                else:
                    arr.append((p,c))
            while arr:
                heapq.heappush(hp, arr.pop())
        return w

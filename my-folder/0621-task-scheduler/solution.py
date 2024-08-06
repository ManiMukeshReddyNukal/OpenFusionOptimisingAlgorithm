class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=[0]*26
        for task in tasks:
            c[ord(task)-ord('A')]+=1
        pq=[-f for f in c if f>0]
        heapq.heapify(pq) 
        time=0
        while pq:
            cycle=n+1
            store=[]
            t=0
            while pq and cycle>0:
                c=-heapq.heappop(pq)
                if c>1:
                    store.append(-(c-1))
                t+=1
                cycle-=1
            for x in store:
                heapq.heappush(pq,x)
            time+=t if not pq else n+1
        return time

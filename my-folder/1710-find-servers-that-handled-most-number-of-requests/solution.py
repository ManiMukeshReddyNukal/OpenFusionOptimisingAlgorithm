class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available=list(range(k))
        heapq.heapify(available)
        busy=[]
        perf=[0]*k
        for i,start in enumerate(arrival):
            while busy and busy[0][0]<=start:
                server_end,server_id=heapq.heappop(busy)
                heapq.heappush(available, i+(server_id-i)%k)
            if available:
                serverid=heapq.heappop(available)%k
                perf[serverid]+=1
                heapq.heappush(busy, (start+load[i],serverid))
        max_requests = max(perf)
        return [i for i in range(k) if perf[i] == max_requests]

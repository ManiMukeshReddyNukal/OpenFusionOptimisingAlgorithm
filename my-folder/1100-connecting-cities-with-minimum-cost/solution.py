class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        graph={}
        for i in range(1,n+1):
            graph[i]=[]
        for s,d,w in connections:
            graph[s].append((d,w))
            graph[d].append((s,w))
        pq=[(0,1)]
        visited=set()
        total=0
        while pq:
            cost,node=heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            total+=cost
            for no,c in graph[node]:
                if no not in visited:
                    heapq.heappush(pq,(c,no))
        return total if len(visited)==n else -1

import heapq
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for i in range(n+1)]
        for e in connections:
            adj[e[0]].append((e[1],e[2]))
            adj[e[1]].append((e[0],e[2]))
        vis = set()
        hp = [(0,1)]
        cost = 0
        while hp and n>0:
            curdist,curnode = heapq.heappop(hp)
            if curnode not in vis:
                vis.add(curnode)
                cost += curdist
                n-=1
            else: continue
            for neigh,w in adj[curnode]:
                if neigh not in vis:
                    heapq.heappush(hp, (w,neigh))
        return cost if n==0 else -1




        # graph={}
        # for i in range(1,n+1):
        #     graph[i]=[]
        # for s,d,w in connections:
        #     graph[s].append((d,w))
        #     graph[d].append((s,w))
        # pq=[(0,1)]
        # visited=set()
        # total=0
        # while pq:
        #     cost,node=heapq.heappop(pq)
        #     if node in visited:
        #         continue
        #     visited.add(node)
        #     total+=cost
        #     for no,c in graph[node]:
        #         if no not in visited:
        #             heapq.heappush(pq,(c,no))
        # return total if len(visited)==n else -1

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges)+1
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        leafnode = 0
        for i in range(n):
            if len(adj[i])==1:
                leafnode = i
                break

        leafnode2 = 0
        vis=set([leafnode])
        q = deque([leafnode])
        while q:
            curnode=q.popleft()
            leafnode2 = curnode
            for neigh in adj[curnode]:
                if neigh not in vis:
                    vis.add(neigh)
                    q.append(neigh)
        
        maxdep = 0
        vis = set([leafnode2])
        q=deque([(leafnode2,0)])
        while q:
            curnode,dep = q.popleft()
            maxdep = max(maxdep,dep)
            for neigh in adj[curnode]:
                if neigh not in vis:
                    vis.add(neigh)
                    q.append((neigh,dep+1))
        return maxdep

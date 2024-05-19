class Solution:
    def canFinish(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[1]].append(e[0])
        vis=set()
        for i in range(n):
            if i in vis: continue
            st = [(i,iter(adj[i]))]
            stset = set([i])
            while st:
                # print([j for j,_ in st])
                curnode, it = st[-1]
                neigh = next(it, None)
                if neigh==None:
                    vis.add(curnode)
                    stset.remove(curnode)
                    st.pop()
                    continue
                if neigh in stset: return False
                if neigh not in vis:
                    stset.add(neigh)
                    st.append((neigh,iter(adj[neigh])))
        return True

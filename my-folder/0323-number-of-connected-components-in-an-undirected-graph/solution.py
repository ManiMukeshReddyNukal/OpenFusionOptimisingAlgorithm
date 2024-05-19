class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        vis = set()
        count = 0
        for i in range(n):
            if i in vis: continue
            count += 1
            st = [i]
            vis.add(i)
            while st:
                curnode = st.pop()
                for neigh in adj[curnode]:
                    if neigh not in vis:
                        vis.add(neigh)
                        st.append(neigh)
        return count

class Solution(object):
    def dfs(self,adj,source,destination,state):
        if state[source] is not None:
            return state[source]
        if not adj[source]:
            return source==destination
        state[source]=False
        for neighbors in adj[source]:
            if not self.dfs(adj,neighbors,destination,state):
                return False
        state[source]=True
        return True


    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
    
        adj=[[] for _ in range(n)]
        for [s,d] in edges:
            adj[s].append(d)
        state=[None]*n
        return self.dfs(adj,source,destination,state)
        

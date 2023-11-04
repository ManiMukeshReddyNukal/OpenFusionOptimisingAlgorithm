class Solution(object):
    def dfs(self, adj, source, destination, state):
        # If state is already computed for this source, return it
        if state[source] is not None:
            return state[source]

        # If there are no outgoing edges from source, it should be the destination
        if not adj[source]:  # Correct way to check for an empty list
            return source == destination

        # Temporarily mark the current source as False (visiting)
        state[source] = False

        # Check all the neighbors
        for neighbor in adj[source]:
            if not self.dfs(adj, neighbor, destination, state):
                return False

        # All neighbors checked and no issues found, so mark as True (finished visiting)
        state[source] = True
        return True

    def leadsToDestination(self, n, edges, source, destination):
        adj = [[] for _ in range(n)]  # Initialize adjacency list
        for edge in edges:
            adj[edge[0]].append(edge[1])  # Populate adjacency list

        # Initialize state list to None for each node
        state = [None] * n
        # Start DFS from the source to destination
        return self.dfs(adj, source, destination, state)


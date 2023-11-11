class Graph(object):

    def __init__(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        """
        self.adj_list=[[] for _ in range(n)]
        for i,j,k in edges:
            self.adj_list[i].append((j,k))

    def addEdge(self, edge):
        """
        :type edge: List[int]
        :rtype: None
        """
        i,j,k=edge
        self.adj_list[i].append((j,k))
        

    def shortestPath(self, node1, node2):
        """
        :type node1: int
        :type node2: int
        :rtype: int
        """
        n=len(self.adj_list)
        pq=[]
        heapq.heappush(pq,(0,node1))
        distance=[float('inf')] * n
        distance[node1]=0
        while pq:
            cost,node=heappop(pq)
            if cost > distance[node]:
                continue
            if node == node2:
                return cost
            for n,c in self.adj_list[node]:
                nc=cost+c
                if nc<distance[n]:
                    distance[n]=nc
                    heappush(pq,(nc,n))
        return -1
# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

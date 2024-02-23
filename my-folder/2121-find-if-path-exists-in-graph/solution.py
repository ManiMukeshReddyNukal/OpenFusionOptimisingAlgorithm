class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        graph=defaultdict(list)
        for [a,b] in edges:
            graph[a].append(b)
            graph[b].append(a)
        q=[]
        q.append(source)
        while q:
            node=q.pop(0)
            if node==destination:
                return True
            while graph[node]:
                q.append(graph[node].pop(0))
        return False

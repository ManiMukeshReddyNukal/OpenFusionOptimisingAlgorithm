class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        paths=[]
        path=[0]
        q=[]
        q.append(path)
        while q:
            route=q.pop(0)
            node=route[-1]
            for cn in graph[node]:
                temp_route=deepcopy(route)
                temp_route.append(cn)
                if cn==len(graph)-1:
                    paths.append(temp_route)
                else:
                    q.append(temp_route)

        return paths

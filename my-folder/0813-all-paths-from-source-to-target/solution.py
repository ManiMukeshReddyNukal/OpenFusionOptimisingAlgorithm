class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        target=len(graph)-1
        results=[]
        def backtrack(curr_node,path):
            if curr_node==target:
                results.append(list(path))
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtrack(next_node,path)
                path.pop()
        path=[0]
        backtrack(0,path)
        return results

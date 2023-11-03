class Solution(object):
    def validPath(self, n, edges, source, destination):
        seen=[False]*n
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        seen[source]=True
        stack=[source]
        while stack:
            curr_node=stack.pop()
            for next_node in graph[curr_node]:
                if next_node == destination:
                    return True
                if not seen[next_node]:
                    seen[next_node]=True
                    stack.append(next_node)
        return seen[destination]
   
        

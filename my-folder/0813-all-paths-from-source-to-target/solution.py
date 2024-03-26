import copy
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        a = [[0]] 
        while a:
            path = a.pop() 
            node = path[-1]  
            if node == len(graph) - 1:
                paths.append(path)
                continue  
            for n in graph[node]:
                new_path = path + [n]  
                a.append(new_path)          
        return paths


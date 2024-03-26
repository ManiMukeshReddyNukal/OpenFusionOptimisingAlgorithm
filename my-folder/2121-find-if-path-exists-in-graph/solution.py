class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        m=defaultdict(list)
        for (s,d) in edges:
            m[s].append(d)
            m[d].append(s)
        stack=[]
        stack.append(source)
        seen=[False]*n
        seen[source]=True
        while stack:
            node=stack.pop()
            for d in m[node]:
                seen[node]=True
                if node==destination:
                    return True
                if not seen[d]:
                    stack.append(d)
        return seen[destination]
                

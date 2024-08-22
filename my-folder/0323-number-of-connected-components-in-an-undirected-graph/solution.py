class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count=0
        visited=set()
        m= defaultdict(list)
        for edge in edges:
            m[edge[0]].append(edge[1])
            m[edge[1]].append(edge[0])
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            count+=1
            q=deque()
            q.append(i)
            while q:
                node = q.pop()
                for adjnode in m[node]:
                    if adjnode not in visited:
                        q.append(adjnode)
                        visited.add(adjnode)
        return count

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        q=deque([(0,x)])
        visited=set()
        while q:
            steps,node=q.popleft()
            visited.add(node)
            if node==y:
                return steps
            if node+1 not in visited:
                q.append((steps+1,node+1))
            if node-1 not in visited:
                q.append((steps+1,node-1))
            if node/5 not in visited and node%5==0:
                q.append((steps+1, node/5))
            if node/11 not in visited and node%11==0:
                q.append((steps+1, node/11))

class Solution:
    def longestIncreasingPath(self, a: List[List[int]]) -> int:
        m = len(a)
        n = len(a[0])
        maxdep = 0

        indeg = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                neighs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for curi,curj in neighs:
                    if 0<=curi<m and 0<=curj<n and a[curi][curj]<a[i][j]:
                        indeg[i][j]+=1
        
        q = deque([(i,j,0) for i in range(m) for j in range(n) if indeg[i][j]==0])

        while q:
            i,j,depth = q.popleft()
            maxdep = depth
            neighs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for curi,curj in neighs:
                    if 0<=curi<m and 0<=curj<n and a[curi][curj]>a[i][j]:
                        indeg[curi][curj]-=1
                        if indeg[curi][curj]==0: q.append((curi,curj,depth+1))
        return maxdep+1



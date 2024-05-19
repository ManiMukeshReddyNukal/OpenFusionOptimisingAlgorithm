class Solution:
    def countPaths(self, a: List[List[int]]) -> int:
        m = len(a)
        n = len(a[0])
        mod = 1000000007
        indeg = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                neighs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for curi,curj in neighs:
                    if 0<=curi<m and 0<=curj<n and a[curi][curj]>a[i][j]:
                        indeg[i][j]+=1
        numpaths = [[0 for j in range(n)] for i in range(m)]

        q = deque([(i,j) for i in range(m) for j in range(n) if indeg[i][j]==0])
        while q:
            i,j = q.popleft()
            neighs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for curi,curj in neighs:
                if 0<=curi<m and 0<=curj<n and a[curi][curj]<a[i][j]:
                    indeg[curi][curj]-=1
                    numpaths[curi][curj]+=numpaths[i][j]+1
                    numpaths[curi][curj] = numpaths[curi][curj]%mod
                    if indeg[curi][curj]==0:
                        q.append((curi,curj))
        # print(numpaths)
        return (sum(sum(numpaths[i]) for i in range(m))+m*n)%mod


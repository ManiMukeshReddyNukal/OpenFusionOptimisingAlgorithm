class UnionFind:
    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a - 1), self.find(b - 1)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf=UnionFind(m*n)
        grid=[[0]*n for _ in range(m)]
        ans=[]
        dir=[(0,1),(1,0),(0,-1),(-1,0)]
        count=0
        for i,j in positions:
            if grid[i][j]:
                ans.append(count)
                continue
            grid[i][j]=1
            count+=1
            for (dx,dy) in dir:
                nx,ny=i+dx,j+dy
                if(0<=nx<m and 0<=ny<n and grid[nx][ny] and uf.union(nx*n+ny,i*n+j)):
                    count-=1
            ans.append(count)
        return ans

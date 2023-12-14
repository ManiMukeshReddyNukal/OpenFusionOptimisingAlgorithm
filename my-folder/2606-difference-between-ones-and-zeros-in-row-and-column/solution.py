class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        colsum=[0]*n
        rowsum=[0]*m
        out=[[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowsum[i]+=grid[i][j]
                colsum[j]+=grid[i][j]
        print(rowsum,colsum)
        for i in range(m):
            for j in range(n):
                out[i][j]=2*rowsum[i]+2*colsum[j]-(m+n)
        return out

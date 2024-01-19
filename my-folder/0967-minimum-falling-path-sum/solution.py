class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[inf]*n for _ in range(m)]
        dp[m-1]=matrix[m-1]
        dir=[[1,-1],[1,0],[1,1]]
        for i in range(m-2,-1,-1):
            for j in range(n-1,-1,-1):
                for x,y in dir:
                    dx=i+x
                    dy=j+y
                    if 0<=dx<m and 0<=dy<n:
                        dp[i][j]=min(dp[i][j],dp[dx][dy]+matrix[i][j])
        print(dp)
        return min(dp[0])

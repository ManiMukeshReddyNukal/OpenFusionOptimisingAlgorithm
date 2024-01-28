class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD=10**9+7
        dp=[[0 for _ in range(n)] for _ in range(m)]
        dp[startRow][startColumn]=1
        count=0
        for k in range(1,maxMove+1):
            temp=[[0 for _ in range(n)] for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i==m-1:
                        count=(count+dp[i][j])%MOD
                    if i==0:
                        count=(count+dp[i][j])%MOD
                    if j==n-1:
                        count=(count+dp[i][j])%MOD
                    if j==0:
                        count=(count+dp[i][j])%MOD
                    temp[i][j]=(((dp[i-1][j] if i>0 else 0)+(dp[i+1][j] if i<m-1 else 0))%MOD + ((dp[i][j+1] if j<n-1 else 0) + (dp[i][j-1] if j>0 else 0))%MOD )% MOD
            dp=temp
        return count




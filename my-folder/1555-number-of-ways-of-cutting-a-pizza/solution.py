class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        def dp(x_s,y_s,cuts):
            DIV=10**9+7
            nonlocal memo
            if (x_s,y_s,cuts) in memo:
                return memo[(x_s,y_s,cuts)]
            if cuts==0:
                if mem[x_s][y_s]>0:
                    return 1
                else:
                    return 0
            ans=0
            for i in range(x_s+1,n):
                if mem[x_s][y_s]-mem[i][y_s]>0:
                    ans+=dp(i,y_s,cuts-1)
            for i in range(y_s+1,m):
                if mem[x_s][y_s]-mem[x_s][i]>0:
                    ans+=dp(x_s,i,cuts-1)
            memo[(x_s,y_s,cuts)]=ans
            return ans%DIV
        n=len(pizza)
        m=len(pizza[0])
        memo={}
        mem=[[0]*(m+1) for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                mem[i][j]=mem[i+1][j]+mem[i][j+1]-mem[i+1][j+1]+(pizza[i][j]=='A')
        return dp(0,0,k-1)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        dp=[[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True
            ans+=1
        for i in range(1,n):
            if s[i]==s[i-1]:
                dp[i-1][i]=True
                ans+=1
        for l in range(3,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if dp[i+1][j-1] and s[i]==s[j]:
                    dp[i][j]=True
                    ans+=1
                else:
                    dp[i][j]=False
                j+=1
        return ans

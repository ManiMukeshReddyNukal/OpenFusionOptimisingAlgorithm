class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        dp=[[False]*n for _ in range(n)]
        ans=[0,0]
        for i in range(n):
            dp[i][i]=True
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=True
                ans=[i,i+1]
        for l in range(2,n):
            for i in range(n-l):
                j=i+l
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                    ans=[i,j]
        i,j=ans
        return s[i:j+1]

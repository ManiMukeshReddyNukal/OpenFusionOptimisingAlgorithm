class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo={}
        def dfs(i,k):
            if (i,k) in memo:
                return memo[(i,k)]
            if i==n-1:
                memo[(i,k)]=True
                return True
            for j in range(k-1,k+2):
                if j>0 and stones[i]+j in mp and dfs(mp[stones[i]+j], j):
                    memo[(i,k)]=True
                    return True
            memo[(i,k)]=False
            return False
        n=len(stones)
        mp={stone:i for i,stone in enumerate(stones)}
        return dfs(0, 0)


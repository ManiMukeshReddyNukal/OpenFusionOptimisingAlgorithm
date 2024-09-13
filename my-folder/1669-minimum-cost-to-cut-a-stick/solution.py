class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        dp={}
        def dfs(l,r):
            if r-l==1:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            res=inf
            for cut in cuts:
                if l<cut<r:
                    res=min(res, dfs(l, cut)+dfs(cut, r)+(r-l))
            dp[(l,r)]=res if res!=inf else 0
            return dp[(l,r)]
        return dfs(0,n)

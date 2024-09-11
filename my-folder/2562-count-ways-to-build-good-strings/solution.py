class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(i):
            if i>high:
                return 0
            ans=0
            if low<=i<=high:
                ans+=1
            ans+=dfs(i+zero)+dfs(i+one)
            return ans%MOD
        MOD=1000000007
        return dfs(0)

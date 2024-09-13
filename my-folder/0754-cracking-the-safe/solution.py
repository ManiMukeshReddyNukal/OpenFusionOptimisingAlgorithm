class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(u):
            for x in range(k):
                ue=u*10+x
                if ue not in visited:
                    visited.add(ue)
                    v=ue%mod
                    dfs(v)
                    ans.append(str(x))
        visited=set()
        mod=10**(n-1)
        ans=[]
        dfs(0)
        ans.append("0"*(n-1))
        return "".join(ans)

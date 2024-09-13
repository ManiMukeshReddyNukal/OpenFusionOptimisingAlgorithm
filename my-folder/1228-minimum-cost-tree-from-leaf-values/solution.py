class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(left,right):
            if left==right:
                return 0,arr[left]
            s,mx=inf,-1
            for k in range(left,right):
                s1,mx1=dfs(left,k)
                s2,mx2=dfs(k+1, right)
                t=s1+s2+mx1*mx2
                if s>t:
                    s=t
                    mx=max(mx1,mx2)
            return s,mx
        return dfs(0,len(arr)-1)[0]

class Solution:
    def climbStairs(self, n: int) -> int:
        d={1:1,2:2}
        def recur(n):
            if n in d:
                return d[n]
            if n==1:
                return 1
            elif n==2:
                return 2
            d[n]=recur(n-1)+recur(n-2)
            return d[n]
        return recur(n)

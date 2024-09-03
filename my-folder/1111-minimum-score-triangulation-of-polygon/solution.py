class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache
        def dp(start,end):
            temp=math.inf
            for i in range(start+1,end):
                temp=min(temp,values[start]*values[i]*values[end]+dp(start, i)+dp(i,end))
            if temp==math.inf:
                return 0
            return temp
        return dp(0,len(values)-1)

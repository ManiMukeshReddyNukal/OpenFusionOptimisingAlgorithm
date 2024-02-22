class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=[0]*(n+1)
        for edge in trust:
            graph[edge[0]]-=1
            graph[edge[1]]+=1
        for i in range(1,n+1):
            if graph[i]==n-1:
                return i
        return -1

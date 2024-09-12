class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs=sorted(zip(startTime,endTime,profit))
        n=len(jobs)
        memo={}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i>=n:
                return 0
            _,end,p=jobs[i]
            idx=bisect_left(jobs,end,lo=i+1,key=lambda x:x[0])
            memo[i]=max(dfs(i+1),p+dfs(idx))
            return memo[i]
        return dfs(0)

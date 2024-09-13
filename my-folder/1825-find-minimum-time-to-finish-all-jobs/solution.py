class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        work=[0]*k
        ans=inf
        def dfs(i):
            nonlocal ans
            if i==len(jobs):
                ans=min(ans, max(work))
                return
            for j in range(k):
                if work[j]+jobs[i]>ans:
                    continue
                work[j]+=jobs[i]
                dfs(i+1)
                work[j]-=jobs[i]
                if work[j]==0:
                    break
        dfs(0)
        return ans

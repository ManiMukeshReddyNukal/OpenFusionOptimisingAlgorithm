class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        mem={}
        def dfs(i):
            if i>=len(arr):
                return 0
            if i in mem:
                return mem[i]
            cur_max=0
            res=0
            for j in range(i,min(i+k,len(arr))):
                cur_max=max(cur_max,arr[j])
                window_size=(j-i+1)
                res=max(res,dfs(j+1)+cur_max*window_size)
            mem[i]=res
            return res

        return dfs(0)
        

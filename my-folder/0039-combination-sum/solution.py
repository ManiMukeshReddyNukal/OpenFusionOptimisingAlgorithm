class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output=[]
        curr=[]
        def dfs(i,curr,currentsum):
            if currentsum==target:
                output.append(curr.copy())
                return  
            if i>=len(candidates) or currentsum>target:
                return
            curr.append(candidates[i])
            dfs(i, curr, currentsum+candidates[i])
            curr.pop()
            dfs(i+1, curr, currentsum)
        dfs(0,[],0)
        return output

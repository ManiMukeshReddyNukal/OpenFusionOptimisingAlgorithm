class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        def backtrack(bal,comb,start):
            if bal==0:
                results.append(list(comb))
                return
            if bal<0:
                return
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                backtrack(bal-candidates[i],comb,i)
                comb.pop()
        backtrack(target,[],0)
        return results

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pmi,pmx=0,-math.inf
        ans,s,smi=-math.inf,0,math.inf
        for num in nums:
            s+=num
            ans=max(ans, s-pmi)
            smi=min(smi,s-pmx)
            pmi=min(pmi,s)
            pmx=max(pmx,s)
        return max(ans,s-smi)

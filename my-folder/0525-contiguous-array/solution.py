class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        ans=s=0
        for i,num in enumerate(nums):
            s+=num if num else -1
            if s in d:
                ans=max(ans, i-d[s])
            else:
                d[s]=i
        return ans


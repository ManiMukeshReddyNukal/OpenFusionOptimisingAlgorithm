class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans=0
        minimump,maximump,left=-1,-1,-1
        for i,num in enumerate(nums):
            if num<minK or num>maxK:
                left=i
            if num==minK:
                minimump=i
            if num==maxK:
                maximump=i
            ans+=max(0,min(minimump, maximump)-left)
        return ans

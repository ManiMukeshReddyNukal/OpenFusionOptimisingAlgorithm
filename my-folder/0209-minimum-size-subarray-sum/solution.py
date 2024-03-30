class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        left=0
        sum=0
        ans=float('inf')
        for i in range(n):
            sum+=nums[i]
            while sum>=target:
                ans=min(ans,i-left+1)
                sum-=nums[left]
                left+=1
        return ans if ans!=float('inf') else 0

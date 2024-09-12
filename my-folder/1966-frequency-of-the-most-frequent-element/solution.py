class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        pre=0
        i=0
        ans=0
        for j,cur in enumerate(nums):
            pre+=cur
            while cur*(j-i+1)>pre+k:
                pre-=nums[i]
                i+=1
            ans=max(ans,j-i+1)
        return ans

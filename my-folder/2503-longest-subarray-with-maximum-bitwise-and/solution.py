class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        v=max(nums)
        count=0
        ans=0
        for num in nums:
            if num==v:
                count+=1
                ans=max(ans,count)
            else:
                count=0
        return ans

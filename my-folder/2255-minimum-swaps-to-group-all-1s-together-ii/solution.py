class Solution:
    def minSwaps(self, nums: List[int]) -> int:
       
        windowsize=sum(nums)
        if windowsize==0 or windowsize==len(nums):
            return 0
        
        n=len(nums)
        initialsum=sum(nums[:windowsize])
        ans=initialsum
        for i in range(windowsize,windowsize+len(nums)):
            initialsum-=nums[(i-windowsize)%n]
            initialsum+=nums[i%n]
            ans=max(initialsum,ans)
        return windowsize-ans

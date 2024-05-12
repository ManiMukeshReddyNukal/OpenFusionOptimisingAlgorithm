class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        i,j=0,0
        minlen = n+1
        cursum = 0
        for j in range(n):
            cursum += nums[j]
            while cursum>=target:
                minlen=min(minlen,j-i+1)
                cursum-=nums[i]
                i+=1
        return minlen if minlen<n+1 else 0


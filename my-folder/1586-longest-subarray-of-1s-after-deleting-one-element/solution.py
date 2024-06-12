class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        zeroes=0
        l=0
        result=0
        for i in range(n):
            if nums[i]==0:
                zeroes+=1
            while zeroes>=2:
                if nums[l]==0:
                    zeroes-=1
                l+=1
            result=max(result,i-l+1)
        return result-1

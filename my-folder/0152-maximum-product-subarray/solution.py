class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        mi=nums[0]
        ma=nums[0]
        result=ma
        for i in range(1,len(nums)):
            curr=nums[i]
            temp_max=max(curr,curr*ma,mi*curr)
            mi=min(curr,curr*ma,mi*curr)
            ma=temp_max
            result=max(ma,result)
        return result

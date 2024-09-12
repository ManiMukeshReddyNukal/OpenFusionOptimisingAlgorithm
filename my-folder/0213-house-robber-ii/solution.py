class Solution:
    def rob(self, nums: List[int]) -> int:
        def roblin(nums):
            if len(nums)==0:
                return
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums[0],nums[1])
            amount=[0]*len(nums)
            amount[0]=nums[0]
            amount[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                amount[i]=max(amount[i-2]+nums[i],amount[i-1])
            return amount[-1]
        if len(nums)==0:
            return
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        return max(roblin(nums[:-1]),roblin(nums[1:]))

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        return max(self.roblin(nums[0:len(nums)-1]),self.roblin(nums[1:]))

    def roblin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print(nums)
        if len(nums)==0:
            return 
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        amount=[0]*(len(nums))
        amount[0]=nums[0]
        amount[1]=max(amount[0],nums[1])
        for i in range(2,len(nums)):
            amount[i]=max(amount[i-1],amount[i-2]+nums[i])
        return amount[-1]

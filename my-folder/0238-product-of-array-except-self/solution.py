class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=[1]*len(nums)
        for i in range(1,len(nums)):
            out[i]=out[i-1]*nums[i-1]
        print(out)
        r=1
        for i in range(len(nums)-2,-1,-1):
            r*=nums[i+1]
            out[i]=out[i]*r 
        return out

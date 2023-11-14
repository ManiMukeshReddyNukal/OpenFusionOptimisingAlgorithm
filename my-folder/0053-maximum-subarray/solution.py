class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=nums[0]
        for num in nums[1:]:
            a=max(num,a+num)
            b=max(b,a)
        return b


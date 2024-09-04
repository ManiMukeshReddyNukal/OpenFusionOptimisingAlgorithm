class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        starti=nums[0]
        while nums[starti]>0:
            nums[starti]=-1*nums[starti]
            starti=abs(nums[starti])
        return abs(starti)

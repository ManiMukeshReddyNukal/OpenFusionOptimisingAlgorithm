class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c in h:
                return [i,h[c]]
            h[nums[i]]=i
        

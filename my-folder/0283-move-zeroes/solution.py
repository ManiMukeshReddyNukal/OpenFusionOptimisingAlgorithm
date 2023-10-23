class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index=0
        for n in nums:
            if n!=0:
                nums[index]=n
                index+=1
        while index<len(nums):
            nums[index]=0
            index+=1
        

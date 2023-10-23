class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        print(nums)
        for i in range(len(nums)/2):
            if(nums[2*i]!=nums[(2*i)+1]):
                print
                return nums[2*i]
        return nums[-1]        
        

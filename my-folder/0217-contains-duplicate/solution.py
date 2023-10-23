class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        et=set(nums)
    
        if len(nums)!=len(et):
            return True
        else : 
            return False

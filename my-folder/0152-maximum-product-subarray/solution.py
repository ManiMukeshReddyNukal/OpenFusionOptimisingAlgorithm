class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far=nums[0]
        min_so_far=nums[0]
        result=max(max_so_far,min_so_far)
        for n in nums[1:]:
            temp_max=max(max_so_far*n,n,min_so_far*n)
            min_so_far=min(n,max_so_far*n,min_so_far*n)
            max_so_far=temp_max
            result=max(max_so_far,result)
        return result

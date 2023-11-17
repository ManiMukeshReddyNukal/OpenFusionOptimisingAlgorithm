class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ar=[]
        for i in range(len(nums)//2):
            ar.append(nums[i]+nums[len(nums)-i-1])
        return max(ar)

        

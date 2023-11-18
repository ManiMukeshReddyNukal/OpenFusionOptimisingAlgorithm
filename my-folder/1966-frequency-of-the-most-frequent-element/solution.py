class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i=j=0
        total=0
        res=0
        while j<len(nums):
            total+=nums[j]
            while ( nums[j] * (j-i+1) > total + k):
                total-=nums[i]
                i+=1
            res=max(res,j-i+1)
            j+=1
        return res


        
        

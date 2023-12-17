class Solution(object):
    def divideArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        out=[]
        i=0
        while i < n:
            if nums[i+2]<= nums[i]+k:
                out.append(nums[i:i+3])
            else:
                return []
            i+=3
        return out
        
            
        

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=1
        high=len(nums)-1
        while (low<=high):
            cur=(low+high)/2
            count=0
            count=sum(num<=cur for num in nums)
            if count>cur:
                duplicate = cur
                high=cur-1
            else:
                low=cur+1
        return duplicate
        

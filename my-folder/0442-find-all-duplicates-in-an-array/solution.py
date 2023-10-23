class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resp=[]
        for i in nums:
            if nums[abs(i)-1]<0:
                resp.append(abs(i))
            else:
                nums[abs(i)-1]=-nums[abs(i)-1]
        return resp

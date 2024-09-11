class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr=[]
        n=len(nums)
        for i in range(n):
            idx=bisect_left(arr,nums[i])
            if idx>=len(arr):
                arr.append(nums[i])
            else:
                arr[idx]=nums[i]
        return len(arr)

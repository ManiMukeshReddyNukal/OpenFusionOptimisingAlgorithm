class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)//3
        s = set()
        for i in range(len(nums)):
            if nums.count(nums[i])>n:
                s.add(nums[i])
        return s

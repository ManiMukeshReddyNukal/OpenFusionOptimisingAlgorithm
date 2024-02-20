class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set=set(nums)
        n=len(nums)+1
        for num in range(n):
            if num not in nums_set:
                return num

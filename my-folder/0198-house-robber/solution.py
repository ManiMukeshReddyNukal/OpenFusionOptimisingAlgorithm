class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        d={}
        def recur(i):
            if i>=n:
                return 0
            if i in d:
                return d[i]
            if i==n-1:
                d[i]=nums[i]
                return nums[i]
            if i==n-2:
                d[i]=max(nums[n-1],nums[n-2])
                return d[i]
            d[i]=max(recur(i+1),recur(i+2)+nums[i])
            return d[i]
        return recur(0)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        @cache
        def dp(i,current_sum):
            if i==len(nums):
                return 1 if current_sum==target else 0
            if (index,current_sum) in memo:
                return memo[(index,current_sum)]
            return dp(i+1,current_sum+nums[i])+dp(i+1, current_sum-nums[i])
        return dp(0,0)

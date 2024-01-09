class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        dp=[defaultdict(int) for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                ans+=dp[j][nums[i]-nums[j]]
                dp[i][nums[i]-nums[j]]+=dp[j][nums[i]-nums[j]]+1
        return ans

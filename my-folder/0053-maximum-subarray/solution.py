class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start=0
        end=0
        max_so_far_value=nums[0]
        max_ending_here_value=nums[0]
        for i in range(1,len(nums)):
            print(i)
            if(nums[i]>max_ending_here_value+nums[i]):
                max_ending_here_value=nums[i]
                start=i
            else:
                max_ending_here_value=max_ending_here_value+nums[i]
            if (max_so_far_value<max_ending_here_value):
                max_so_far_value=max_ending_here_value
                end=i
        return max_so_far_value




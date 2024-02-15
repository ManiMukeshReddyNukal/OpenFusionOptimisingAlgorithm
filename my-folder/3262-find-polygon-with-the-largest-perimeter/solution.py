class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=-1
        previous_element_sum=0
        for num in nums:
            if num<previous_element_sum:
                ans=num+previous_element_sum
            previous_element_sum+=num
        return ans
         

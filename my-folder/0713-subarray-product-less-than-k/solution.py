class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l=0
        if k <= 1:
            return 0
        n=len(nums)
        product=1
        count=0
        for r,num in enumerate(nums):
            product*=num
            while product>=k:
                product=product/nums[l]
                l+=1
            count+=r-l+1
        return count


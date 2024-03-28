from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        n=len(nums)
        c=defaultdict(int)
        le=0
        for r, num in enumerate(nums):
            c[num]=c.get(num,0)+1
            while c[num]>k:
                print(r,l)
                c[nums[l]]=c.get(nums[l],0)-1
                l+=1
            le=max(le,r-l+1)
        return le



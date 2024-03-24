class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l=1
        r=len(nums)-1
        while l<=r:
            c=(l+r)//2
            count=0
            count=sum(num<=c for num in nums)
            if count>c:
                duplicate=c
                r=c-1
            else:
                l=c+1
        return duplicate

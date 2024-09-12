class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            pre=inf
            count=0
            for cur in nums:
                pre+=cur
                if pre>mid:
                    pre=cur
                    count+=1
            return count<=k
        left,right=max(nums),sum(nums)
        return left + bisect_left(range(left,right+1),True,key=check)

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(diff):
            count=0
            pre=-diff
            for cur in price:
                if cur-pre>=diff:
                    count+=1
                    pre=cur
            return count>=k
        price.sort()
        left,right=0,price[-1]-price[0]
        while left<right:
            mid=(left+right+1)//2
            if check(mid):
                left=mid
            else:
                right=mid-1
        return left

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        l=1
        r=max(piles)
        midSpeed=r
        while l<=r:
            midSpeed=l+(r-l)//2
            hourspent=0
            for p in piles:
                hourspent += p // midSpeed + 1 if p % midSpeed > 0 else p //midSpeed

            if hourspent>h:
                l=midSpeed+1
            else:
                r=midSpeed-1
        return l

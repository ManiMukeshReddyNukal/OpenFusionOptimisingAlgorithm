class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        l=1
        r=max(piles)
        midspeed=0
        while l<=r:
            midspeed=(l+r)//2
            hoursspent=0
            for p in piles:
                hoursspent+=(p//midspeed)+ 1 if p%midspeed>0 else p//midspeed
            if hoursspent>h:
                l=midspeed+1
            else:
                r=midspeed-1
        return l

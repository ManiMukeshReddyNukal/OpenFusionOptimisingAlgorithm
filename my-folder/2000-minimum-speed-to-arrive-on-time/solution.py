class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(v):
            s=0
            for i,d in enumerate(dist):
                t=d/v
                s+=t if len(dist)-1==i else ceil(t)
            return s<=hour
        ans=bisect_left(range(1,10**7+1), True, key=check)+1
        return -1 if ans==10**7+1 else ans

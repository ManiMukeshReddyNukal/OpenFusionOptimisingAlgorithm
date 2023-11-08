class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x=abs(fx-sx)
        y=abs(fy-sy)
        if x==0 and y==0 and t==1:
            return False
        return t>=max(x,y)

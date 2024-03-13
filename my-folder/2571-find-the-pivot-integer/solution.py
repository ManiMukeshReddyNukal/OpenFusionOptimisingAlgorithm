class Solution:
    def pivotInteger(self, n: int) -> int:
        l=1
        r=n
        sl=l
        sr=r
        if n==1:
            return n
        while l<r:
            if sl<sr:
                sl+=l+1
                l+=1
            else:
                sr+=r-1
                r-=1
            if sl==sr and l+1==r-1:
                return l+1
        return -1

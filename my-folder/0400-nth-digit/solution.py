class Solution:
    def findNthDigit(self, n: int) -> int:
        l=1
        digit=9
        while n>digit*l:
            n-=l*digit
            l+=1
            digit*=10
        start_num=10**(l-1)
        dividend,remainder=divmod(n,l)
        if remainder==0:
            return int(str(start_num+dividend-1)[-1])
        else:
            return int(str(start_num+dividend)[remainder-1])

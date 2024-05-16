class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors=[]
        reversefactors=[]
        count=0
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                factors.append(i)
                reversefactors.append(n//i)
            if len(factors)==k:
                return factors[-1]
        reversefactors=reversefactors[::-1]
        if factors[-1]==reversefactors[0]:
            reversefactors.pop(0)
        factors.extend(reversefactors)
        if len(factors)>=k:
            return factors[k-1]
        return -1


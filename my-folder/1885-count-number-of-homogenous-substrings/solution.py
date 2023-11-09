class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s+" "
        ans=0
        i=1
        ar=[]
        for j in range(len(s)-1):
            if s[j+1]==s[j]:
                i+=1
            else:
                ar.append(i)
                i=1
        print(ar)
        for k in ar:
            c=(k*(k+1)/2)% (10**9 + 7)
            ans = (ans + c ) % (10**9 + 7)
        return ans

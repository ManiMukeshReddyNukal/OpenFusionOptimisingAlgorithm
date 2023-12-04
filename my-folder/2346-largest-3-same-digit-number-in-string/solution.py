class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        i=0
        out="-1"
        while i<len(num)-2:
            if num[i]==num[i+1]==num[i+2]:
                if (int(num[i:i+3]) > int(out)):
                    out=num[i:i+3]
            i+=1
        if int(out)==-1:
            return ""
        else:
            return out

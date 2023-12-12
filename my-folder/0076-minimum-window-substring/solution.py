class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tmap={}
        for c in t:
            tmap[c]=tmap.get(c,0)+1
        uniq=len(tmap)
        found=0
        l=r=0
        ans=float("inf"),None,None
        windowcount={}
        while r<len(s):
            char=s[r]
            windowcount[char]=windowcount.get(char,0)+1
            if char in tmap and windowcount[char]==tmap[char]:
                found+=1
            while l<=r and found==uniq:
                char=s[l]
                if r-l+1<ans[0]:
                    ans=(r-l+1,l,r)
                windowcount[char]-=1
                if char in tmap and windowcount[char]<tmap[char]:
                    found-=1
                l+=1
            r+=1
        return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
        

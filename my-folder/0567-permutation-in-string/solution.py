class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1map={}
        for s in s1:
            s1map[s]=s1map.get(s,0)+1
        s2map={}
        m=len(s1)
        n=len(s2)
        if n<m:
            return False
        i=0
        j=m
        for k in range(m):
            s2map[s2[k]]=s2map.get(s2[k],0)+1
        if s1map==s2map:
                return True
        while j<n:
            s2map[s2[j]]=s2map.get(s2[j],0)+1
            if s2map[s2[i]] == 1:
                del s2map[s2[i]]
            else:
                s2map[s2[i]] -= 1
            if s1map==s2map:
                return True
            i+=1
            j+=1
            
        return False
        

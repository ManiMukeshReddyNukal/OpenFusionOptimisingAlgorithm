class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v_l=[]
        v_p=[]
        t=list(s)
        for i,c in enumerate(s):
            if c.lower() in { 'a','e','i','o','u'}:
                v_l.append(c)
                v_p.append(i)
        print(v_l)
        v_l.sort()
        print(v_l)
        for i,char in zip(v_p,v_l):
            t[i]=char
        return ''.join(t)

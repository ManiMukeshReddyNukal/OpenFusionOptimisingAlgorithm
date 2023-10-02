class Solution(object):
    def customSortString(self, order, s):
        output=''
        for a in order:
            if a in s:
                output+=a*(s.count(a))
        for b in s :
            if b not in order :
                output+=b
        return output            

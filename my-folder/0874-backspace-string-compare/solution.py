class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(S):
            ans=[]
            for c in S:
                if c!='#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return "".join(ans)
        return build(s)==build(t)

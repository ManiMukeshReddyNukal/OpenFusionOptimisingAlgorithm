class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        def recursivefunction(st,l,r):
            if l==r==n:
                ans.append("".join(st))
                return
            if l<n:
                st.append("(")
                recursivefunction(st,l+1,r)
                st.pop()
            if r<l:
                st.append(")")
                recursivefunction(st,l,r+1)
                st.pop()
        recursivefunction([],0,0)
        return ans

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        output=[]
        curr=[]
        def backtrack(open,close):
            if open==close==n:
                output.append("".join(curr))
                return
            if open<n:
                curr.append("(")
                backtrack(open+1,close)
                curr.pop()
            if close<open:
                curr.append(")")
                backtrack(open,close+1)
                curr.pop()
        backtrack(0,0)
        return output
        

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        m={")":"(","}":"{","]":"["}
        for c in s:
            if c in m:
                top=stack.pop() if stack else '#'
                if top!=m[c]:
                    return False
            else:
                stack.append(c)
        return not stack

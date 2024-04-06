class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        l=[]
        lastparenthesis=""
        for i in range(len(s)):
            if s[i]=="(":
                stack.append((i))
            elif s[i]==")":
                if len(stack)>0:
                    stack.pop(-1)
                else :
                    l.append(i)
        out=""
        si=0
        stack=stack+l
        stack.sort()
        for i in range(len(stack)):
            out=out+s[si:stack[i]]
            si=stack[i]+1
        out=out+s[si:len(s)+1]
        return out

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        eq=["+","-","*","/"]
        for c in tokens:
            if c not in eq:
                stack.append(c)
            else:
                if c=="+":
                    s=int(stack.pop())+int(stack.pop())
                    stack.append(s)
                elif c=="-":
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(b-a)
                elif c=="*":
                    stack.append(int(stack.pop())*int(stack.pop()))
                elif c=="/":
                    a=int(stack.pop())
                    b=int(stack.pop())
                    stack.append(int(float(b)/a))
        return int(stack.pop())
        

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        def append(operator,operand):
            if operator=="+":
                stack.append(operand)
            elif operator=="-":
                stack.append(-operand)
            elif operator=="/":
                a=stack.pop()
                r=int(abs(a)/operand)
                if a<0: stack.append(-r)
                else: stack.append(r)
            elif operator=="*":
                stack.append(stack.pop() * operand)
        operand,operator=0,"+"
        for c in s:
            if c in "0123456789":
                operand=operand*10+int(c)
            elif c in "+-/*":
                append(operator,operand)
                operand,operator=0,c
        append(operator,operand)
        return sum(stack)
        

class Solution:
    def calculate(self, s: str) -> int:
        val=[]
        sign=[]
        operand=0
        result=0
        sg=+1
        for c in s:
            if c.isdigit():
                operand=operand*10+int(c)
            elif c == "+":
                result+=sg*operand
                # reset 
                sg=+1
                operand=0
            elif c == "-":
                result+=sg*operand
                sg=-1
                operand=0
            elif c == "(":
                val.append(result)
                result=0
                sign.append(sg)
                sg=+1
            elif c == ")":
                result+=sg*operand
                result*=sign.pop()
                result+=val.pop()
                operand=0
        return result+sg*operand

                
           


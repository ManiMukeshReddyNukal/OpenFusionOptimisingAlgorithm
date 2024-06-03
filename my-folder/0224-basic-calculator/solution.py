class Solution:
    def calculate(self, s: str) -> int:
        val=[]
        sign=[]
        operand=0
        sg=+1
        result=0
        for c in s:
            if c.isdigit():
                operand=operand*10+int(c)
            elif c=="+":
                result+=sg*operand
                operand=0
                sg=+1
            elif c=="-":
                result+=sg*operand
                operand=0
                sg=-1
            elif c=="(":
                val.append(result)
                sign.append(sg)
                result=0
                sg=+1
            elif c==")":
                result+=sg*operand
                result*=sign.pop()
                result+=val.pop()
                operand=0
        return result+sg*operand

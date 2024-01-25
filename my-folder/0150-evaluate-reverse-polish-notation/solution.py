class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for o in tokens:
            v=0
            if o not in ["+","-","*","/"]:
                v=int(o)
            elif o=="+":
                v=s.pop()+s.pop()
            elif o=="-":
                dum=s.pop()
                v=s.pop()-dum
            elif o=="*":
                v=s.pop()*s.pop()
            elif o=="/":
                div=s.pop()
                v=int(s.pop()/div)
            s.append(v)
        return s.pop()

class Solution:
    def minimizeResult(self, expression: str) -> str:
        s=expression.split("+")
        custom_comporater=lambda s: eval(s.replace('(','*(').replace(')',')*').strip("*"))
        lft=[s[0][0:i] + "(" + s[0][i:] for i in range(len(s[0]))]
        rgt=[s[1][0:i] + ")" + s[1][i:] for i in range(1,len(s[1])+1)]
        print(lft)
        print(rgt)
        return min([l+'+'+r for l in lft for r in rgt], key=custom_comporater )

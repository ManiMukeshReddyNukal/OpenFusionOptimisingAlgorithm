class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        def findint(s, begin, end):
            val = 0
            power = 1
            for i in range(end,begin-1,-1):
                val += power*int(s[i])
                power*=10
            return val
        def evalmultdiv(s, begin, end):
            ind = begin
            val = 1
            while ind<=end:
                sign = '*'
                if s[ind]=='/':
                    ind+=1
                    sign='/'
                if s[ind]=='*':
                    ind+=1
                    sign='*'
                i,j=ind,ind
                while j<=end and s[j] not in '*/':
                    j+=1
                if sign == '*': val = val*findint(s,i,j-1)
                if sign == '/': val = val//findint(s,i,j-1)
                ind = j
            return val

        vals = []
        ind = 0
        val = 0
        while ind<len(s):
            sign = '+'
            if s[ind]=='-':
                sign = '-'
                ind+=1
            if s[ind]=='+': ind+=1
            i,j=ind,ind
            while j<len(s) and s[j] not in '+-':
                j+=1
            if sign=='+':
                val += evalmultdiv(s,i,j-1)
            else:
                val -= evalmultdiv(s,i,j-1)
            ind=j
        return val



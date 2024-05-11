class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        closeind = {}
        st = []
        for i in range(len(s)):
            if s[i] == '(': st.append(i)
            if s[i] == ')':
                closeind[st[-1]] = i
                st.pop()
        def findval(s,begin,end):
            if begin>end or begin>=len(s): return 0
            # if s[begin]=='(': return findval(s,begin+1,closeind[begin]-1)
            val = 0
            ind = begin
            while ind<=end:
                sign='+'
                if s[ind]=='-':
                    sign='-'
                    ind+=1
                if s[ind]=='+':
                    ind+=1
                i,j=ind,ind
                while j<len(s) and s[j] not in '+-()':
                    j+=1
                curval = 0
                if s[i]=='(':
                    curval = findval(s,j+1,closeind[i]-1)
                    ind = closeind[i]+1
                else:
                    # print(i,j)
                    curval = int(s[i:j])
                    ind = j
                if sign=='+':
                    val += curval
                if sign=='-':
                    val -= curval
            return val
        return findval(s,0,len(s)-1)

                
           


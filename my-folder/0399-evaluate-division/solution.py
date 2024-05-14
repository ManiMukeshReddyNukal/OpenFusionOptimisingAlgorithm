class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        dic={}
        def find(x):
            if x not in dic:
                dic[x]=(x,1)
            base,w=dic[x]
            if base!=x:
                new_root,w2=find(base)
                dic[x]=(new_root,w2*w)
            return dic[x]
        def union(x,y,value):
            b_x,w_x=find(x)
            b_y,w_y=find(y)
            if b_x!=b_y:
                dic[b_x]=(b_y,(value*w_y)/w_x)
        for [a,b],c in zip(equations,values):
            union(a,b,c)
        out=[]
        for n,d in queries:
            if n not in dic or d not in dic:
                out.append(-1)
            elif n==d:
                out.append(1)
            else:
                b_x,w_x=find(n)
                b_y,w_y=find(d)
                if b_x!=b_y:
                    out.append(-1)
                else:
                    out.append(w_x/w_y)
        return out

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
            root,weight=dic[x]
            if root!=x:
                new_root,new_weight=find(root)
                dic[x]=(new_root,weight*new_weight)
            return dic[x]
        def union(x,y,value):
            g_1,w_1=find(x)
            g_2,w_2=find(y)
            if g_1!=g_2:
                dic[g_1]=(g_2,((value*w_2)/w_1))
        res=[]
        for (div,dis),value in zip(equations,values):
            union(div,dis,value)
        for (div,dis) in queries:
            if div not in dic or dis not in dic:
                res.append(-1)
                continue
            if div==dis:
                res.append(1)
                continue
            g_1,w_1=find(div)
            g_2,w_2=find(dis)
            if g_1!=g_2:
                res.append(-1)
                continue
            res.append(w_1/w_2)
        return res


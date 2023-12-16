class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        m=[[0,0,0,0],[1,1,1,1],[2,4,8,6],[3,9,7,1],[4,6,4,6],[5,5,5,5],[6,6,6,6],[7,9,3,1],[8,4,2,6],[9,1,9,1]]
        out=[]
        for i in range(len(variables)):
            a,b,c,d=variables[i]
            v=m[a%10][b%4-1]
            if (v**c)%d==target:
                out.append(i)
        return out
        

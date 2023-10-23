class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        out=[]
        if len(original)!=m*n:
            return out
        for i in range(m):
            ar=[]
            for j in range(n):
                ar.append(original[(i*n)+j])
            out.append(ar)
        return out
        

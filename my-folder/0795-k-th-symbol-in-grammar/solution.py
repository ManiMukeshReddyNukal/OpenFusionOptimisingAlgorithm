class Solution(object):
    def depthFirstSearch(self,n,k,rootval):
        if n==1:
            return rootval
        totalnodes=2**(n-1)
        if k > (totalnodes/2):
            nextRootVal=1 if rootval is 0 else 0
            return self.depthFirstSearch(n-1,k-(totalnodes/2),nextRootVal)
        else:
            nextRootVal=0 if rootval is 0 else 1
            return self.depthFirstSearch(n-1,k,nextRootVal)

    def kthGrammar(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        return self.depthFirstSearch(n,k,0)

        

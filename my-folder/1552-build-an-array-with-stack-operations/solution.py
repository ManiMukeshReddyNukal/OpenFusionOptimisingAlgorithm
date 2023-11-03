class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        i=0
        for num in target:
            while i<num-1:
                ans.append("Push")
                ans.append("Pop")
                i+=1
            ans.append("Push")
            i+=1
        return ans
        

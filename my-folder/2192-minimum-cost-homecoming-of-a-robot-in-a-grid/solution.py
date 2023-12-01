class Solution(object):
    def minCost(self, startPos, homePos, rowCosts, colCosts):
        """
        :type startPos: List[int]
        :type homePos: List[int]
        :type rowCosts: List[int]
        :type colCosts: List[int]
        :rtype: int
        """
        s=0
        if startPos[0]>homePos[0]:
            s+=sum(rowCosts[homePos[0]:startPos[0]])
        else:
            s+=sum(rowCosts[startPos[0]+1:homePos[0]+1])
        if startPos[1]>homePos[1]:
            s+=sum(colCosts[homePos[1]:startPos[1]])
        else:
            s+=sum(colCosts[startPos[1]+1:homePos[1]+1])
        return s
        

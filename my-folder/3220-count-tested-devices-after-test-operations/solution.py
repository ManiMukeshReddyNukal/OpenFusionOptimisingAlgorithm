class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        tested=0
        for b in batteryPercentages:
            b=b-tested
            if b>0:
                tested+=1
        return tested
                
        

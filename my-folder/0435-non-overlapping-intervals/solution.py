class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        ans=0
        k=float('-inf')
        for a,b in intervals:
            if a>=k:
                k=b
            else:
                ans+=1
        return ans

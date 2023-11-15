class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key=lambda x:x[1])
        k=float('-inf')
        for a,b in intervals:
            if a>=k:
                k=b
            else:
                return False
        return True

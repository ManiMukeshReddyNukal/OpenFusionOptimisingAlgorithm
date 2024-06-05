class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sortedintervals=sorted((interval[0],i) for i,interval in enumerate(intervals) )
        result=[]
        for start,end in intervals:
            idx=bisect_left(sortedintervals, (end,))
            if idx<len(sortedintervals):
                result.append(sortedintervals[idx][1])
            else:
                result.append(-1)
        return result

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        inserted=False
        for s,e in intervals:
            if e<newInterval[0]:
                result.append([s,e])
            elif s>newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                    inserted=True
                result.append([s,e])
            else:
                newInterval[0]=min(newInterval[0],s)
                newInterval[1]=max(newInterval[1], e)
        if not result or not inserted:
            result.append(newInterval)
        return result

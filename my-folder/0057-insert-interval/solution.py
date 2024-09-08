class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        added=False
        for s,e in intervals:
            if e<newInterval[0]:
                result.append([s,e])
            elif s>newInterval[1]:
                if not added:
                    result.append(newInterval)
                    added=True
                result.append([s,e])
            else:
                newInterval=[min(newInterval[0], s),max(newInterval[1], e)]
        if not added:
            result.append(newInterval)
        return result

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        resp=[]
        for interval in intervals:
            if not resp or resp[-1][1]<interval[0]:
                resp.append(interval)
            else:
                resp[-1][1]=max(resp[-1][1],interval[1])
        return resp

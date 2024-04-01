class Solution:
    def merge (self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        for inte in intervals:
            if not merged or merged[-1][1]<inte[0]:
                merged.append(inte)
            else:
                merged[-1][1]=max(inte[1],merged[-1][1])
        return merged

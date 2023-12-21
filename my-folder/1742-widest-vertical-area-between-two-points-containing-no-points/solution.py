class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x=[point[0] for point in points]
        x.sort()
        max_diff=0
        for i in range(len(x)-1):
            max_diff=max(max_diff,x[i+1]-x[i])
        return max_diff

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        marea=0
        stack=[]
        n=len(heights)
        for i,h in enumerate(heights):
            startIndex=i
            while stack and h<stack[-1][1]:
                startIndex,height=stack.pop()
                marea=max(height*(i-startIndex),marea)
            stack.append([startIndex,h])
        while stack:
            startIndex,height=stack.pop()
            marea=max(height*(n-startIndex),marea)
        return marea


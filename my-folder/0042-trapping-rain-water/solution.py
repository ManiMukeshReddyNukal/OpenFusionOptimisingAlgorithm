class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[0]*n
        right=[0]*n
        maxsofarl=0
        maxsofarr=0
        for i in range(n):
            maxsofarl=max(maxsofarl,height[i])
            maxsofarr=max(maxsofarr, height[n-i-1])
            left[i]=maxsofarl
            right[n-i-1]=maxsofarr
        ans=0
        for i in range(n):
            ans+=(min(left[i],right[i])-height[i])
        return ans

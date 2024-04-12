class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        left_min,right_min=[0]*n,[0]*n
        left_min[0],right_min[n-1]=height[0],height[n-1]
        for i in range(1,n):
            left_min[i]=max(left_min[i-1],height[i])
            right_min[n-i-1]=max(right_min[n-i],height[n-i-1])
        ans=0
        for i in range(1,n-1):
            ans+=(min(left_min[i],right_min[i])-height[i])
        return ans


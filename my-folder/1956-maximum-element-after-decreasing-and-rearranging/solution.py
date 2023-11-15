class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        arr.sort()
        ans=1
        for i in range(1,n):
            if arr[i] >= ans+1:
                ans+=1
        return ans

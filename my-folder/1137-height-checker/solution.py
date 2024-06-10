class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        def bubblesort(arr):
            n=len(arr)
            for i in range(n):
                for j in range(n-i-1):
                    if arr[j]>arr[j+1]:
                        arr[j],arr[j+1]=arr[j+1],arr[j]
            return arr
        sorted_height=heights[:]
        sorted_height=bubblesort(sorted_height)
        count=0
        for i in range(len(heights)):
            if heights[i]!=sorted_height[i]:
                count+=1
        return count

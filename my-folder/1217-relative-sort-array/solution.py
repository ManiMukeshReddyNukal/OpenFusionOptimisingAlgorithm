class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_element=max(arr1)
        count=[0]*(max_element+1)
        for i in arr1:
            count[i]+=1
        result=[]
        for c in arr2:
            while count[c]>0:
                result.append(c)
                count[c]-=1
        for i in range(max_element+1):
            while count[i]>0:
                result.append(i)
                count[i]-=1
        return result

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count=collections.Counter(arr)
        sorted_items =sorted(count.items(),key=lambda x:x[1])
        count=0
        for (key,value) in sorted_items:
            print(key,value)
            if k<value:
                return len(sorted_items)-count
            k-=value
            count+=1
        return 0

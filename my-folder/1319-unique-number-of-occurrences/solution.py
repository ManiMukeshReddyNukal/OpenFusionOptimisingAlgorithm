class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=collections.Counter(arr)
        l=s.values()
        return len(l)==len(set(l))

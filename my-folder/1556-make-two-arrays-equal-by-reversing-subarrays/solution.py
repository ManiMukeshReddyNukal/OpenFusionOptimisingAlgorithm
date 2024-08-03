class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t=Counter(target)
        a=Counter(arr)
        return True if t==a else False

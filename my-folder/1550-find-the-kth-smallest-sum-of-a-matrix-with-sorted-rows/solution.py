class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        pre=[0]
        for row in mat:
            pre=sorted(a+b for a in pre for b in row[:k])[:k]
        return pre[-1]

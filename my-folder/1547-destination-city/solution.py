class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start=set()
        dest=set()
        for i,j in paths:
            start.add(i)
            dest.add(j)
        return next(iter(dest-start))

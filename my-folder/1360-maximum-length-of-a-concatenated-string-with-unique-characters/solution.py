class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charset=set()
        def overlap(charset,s):
            c=Counter(s)+Counter(charset)
            return max(c.values())>1
        def backtrack(i):
            if len(arr)==i:
                return len(charset)
            res=0
            if not overlap(charset,arr[i]):
                for c in arr[i]:
                    charset.add(c)
                res=backtrack(i+1)
                for c in arr[i]:
                    charset.remove(c)
            return max(res,backtrack(i+1))
        return backtrack(0)



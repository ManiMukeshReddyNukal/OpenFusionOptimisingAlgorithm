class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        stack=[]
        for st in s:
            if st=="(":
                stack.append(st)
            elif st==")":
                stack.pop()
            count=max(count,len(stack))
        return count

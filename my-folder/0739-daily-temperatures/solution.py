class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        ans=[0]*n
        stack=[]
        for i,temp in enumerate(temperatures):
            while len(stack)>0 and temperatures[stack[-1]]<temp:
                idx=stack.pop()
                ans[idx]=i-idx
            stack.append(i)
        return ans

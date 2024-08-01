class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[i for i in range(1,n+1)]
        out=[]
        index=k-1
        factorial=math.factorial(n)
        while nums:
            factorial=factorial//len(nums)
            i=index//factorial
            num=nums.pop(i)
            out.append(str(num))
            index=index%factorial
        return "".join(out)
            

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n=max(nums)
        freq=[0]*(n+1)
        for i in nums:
            freq[i]+=1
        out=[[]]
        for i in range(n+1):
            j=0
            while freq[i]>0:
                if j>len(out)-1:
                    out.append([])
                out[j].append(i)
                j+=1
                freq[i]-=1
        return out
        

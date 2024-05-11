class Solution:
    def minSwaps(self, data: List[int]) -> int:
        k=sum(data)
        noofzeroes=k-sum(data[:k])
        j=k
        i=0
        ans=noofzeroes
        while j<len(data):
            if data[j]==0:
                noofzeroes+=1
            if data[i]==0:
                noofzeroes-=1
            i+=1
            j+=1
            ans=min(noofzeroes,ans)
        return ans

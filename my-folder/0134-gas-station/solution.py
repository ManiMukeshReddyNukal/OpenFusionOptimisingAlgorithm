class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        i=j=n-1
        count=0
        s=0
        while count<n:
            s+=gas[j]-cost[j]
            count+=1
            j=(j+1)%n
            while s<0 and count<n:
                i-=1
                s+=gas[i]-cost[i]
                count+=1
        return -1 if s<0 else i

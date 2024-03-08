class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c={}
        for num in nums:
            if num in c:
                c[num]+=1
            else:
                c[num]=1
        max_freq=0
        count=0
        for k in c.values():
            max_freq=max(k,max_freq)
        for k in c.values():
            if k==max_freq:
                count+=1
        return count*max_freq

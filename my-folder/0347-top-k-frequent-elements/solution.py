class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        s={}
        for i in nums:
            s[i]=s.get(i,0)+1
        sp = sorted(s.items(), key=lambda item: item[1], reverse=True)
        ot=[]
        print(s)
        print(sp)
        return [key for key, _ in list(sp)[:k]]

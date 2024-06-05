class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        q=deque()
        for i in range(k):
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for i in range(k,len(nums)):
            if q and q[0]==i-k:
                q.popleft()
            while q and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res

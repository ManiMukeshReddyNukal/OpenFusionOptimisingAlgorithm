class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def solve(nums,k):
            n=len(nums)
            left=[0]*k
            right=[]
            mini = sys.maxsize
            for i in range(k-1,-1,-1):
                mini=min(mini,nums[i])
                left[i]=mini
            print(left)
            mini=sys.maxsize
            for i in range(k,n):
                mini=min(mini,nums[i])
                right.append(mini)
            print(right)
            ans=0
            for j in range(len(right)):
                cur_min=right[j]
                i=bisect_left(left,cur_min)
                size = (k+j)-i+1
                ans=max(ans,cur_min*size)
            return ans
        return max(solve(nums,k),solve(nums[::-1],len(nums)-k-1))



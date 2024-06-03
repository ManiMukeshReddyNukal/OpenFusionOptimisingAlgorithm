class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash=defaultdict(int)
        hash[0]=1
        res=0
        cur_sum=0
        for num in nums:
            cur_sum+=num
            diff_sum=cur_sum-k
            res+=hash[diff_sum]
            hash[cur_sum]+=1
        return res


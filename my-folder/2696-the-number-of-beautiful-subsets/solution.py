class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def getcount(i,count):
            if i==len(nums):
                return 1
            res=getcount(i+1,count)
            if not count[nums[i]+k] and not count[nums[i]-k]:
                count[nums[i]]+=1
                res+=getcount(i+1, count)
                count[nums[i]]-=1
            return res
        return getcount(0, defaultdict(int))-1

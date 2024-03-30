class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.getsubarrayswithAtmostKDistinct(nums,k)-self.getsubarrayswithAtmostKDistinct(nums,k-1)
    def getsubarrayswithAtmostKDistinct(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        left=0
        freq=collections.defaultdict(int)
        for right in range(n):
            freq[nums[right]]+=1
            while len(freq)>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
            count+=right-left+1
        return count
    

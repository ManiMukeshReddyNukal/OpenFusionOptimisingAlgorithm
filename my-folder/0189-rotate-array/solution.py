class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        start,count=0,0
        while count<n:
            current,value=start,nums[start]
            while True:
                next_idx=(current+k)%n
                nums[next_idx],value=value,nums[next_idx]
                current=next_idx
                count+=1
                if start==current:
                    break
            start+=1

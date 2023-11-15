class Solution(object):
    def sortedSquares(self, nums):
        i = 0
        j = maxindex = len(nums) - 1
        op = [0] * len(nums)
        while i <= j:
            lq = nums[i] ** 2
            rq = nums[j] ** 2
            if lq > rq:
                op[maxindex] = lq
                i += 1
            else:
                op[maxindex] = rq
                j -= 1
            maxindex -= 1
        return op


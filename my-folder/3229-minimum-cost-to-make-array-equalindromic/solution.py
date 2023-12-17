class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        cases=set()
        def getMedian(nums):
            if n%2==1:
                return set([nums[n//2]])
            else:
                return set([nums[n//2],nums[n//2-1]])
        def getSum(palindrome):
            return sum(abs(num-palindrome) for num in nums)
        def getNearestPalindrome(l):
            out=set()
            for e in l:
                while str(e)!=str(e)[::-1]:
                    e-=1
                out.add(e)
            for e in l:
                while str(e)!=str(e)[::-1]:
                    e+=1
                out.add(e)
            return out
        cases.update(getMedian(nums))
        palindromes=getNearestPalindrome(cases)
        return min([getSum(p) for p in palindromes])

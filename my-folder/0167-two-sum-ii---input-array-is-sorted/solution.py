class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # nu={n:i for i,n in enumerate(numbers)}
        # for i in nu:
        #     if target-i in nu:
        #         return sorted([nu[i]+1,nu[target-i]+1])
        i=0
        j=len(numbers)-1
        while numbers[i]+numbers[j]!=target:
            if numbers[i]+numbers[j]>target:
                j-=1
            if numbers[i]+numbers[j]<target:
                i+=1
        return [i+1,j+1]


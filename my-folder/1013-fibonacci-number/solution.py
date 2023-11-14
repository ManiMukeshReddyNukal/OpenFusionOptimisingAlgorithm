class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        cache = [0]*(n+1)
        cache[1]=1
        for i in range(2,n+1):
            cache[i]=cache[i-1]+cache[i-2]
        return cache[n]



# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         if n<=1:
#             return n
#         return self.fib(n-1)+self.fib(n-2)

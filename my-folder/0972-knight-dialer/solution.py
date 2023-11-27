class Solution(object):
    def knightDialer(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD=10**9+7
        dic = { 0: [4, 6],1: [6, 8],2: [7, 9],3: [4, 8],4: [3, 9, 0],5: [],6: [1, 7, 0],7: [2, 6],8: [1, 3],9: [2, 4] }
        memo={}
        def dp(position,steps):
            if steps==0:
                return 1
            if (position,steps) in memo:
                return memo[(position,steps)]
            val=0
            for p in dic[position]:
                val=(val+dp(p,steps-1))%MOD
            memo[(position,steps)]=val
            return val
        ans=0
        for start in range(10):
            ans=(ans+dp(start,n-1))%MOD
        return ans



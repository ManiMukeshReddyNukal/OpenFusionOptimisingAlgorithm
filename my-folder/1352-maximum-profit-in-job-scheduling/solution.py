class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type profit: List[int]
        :rtype: int
        """
        n=len(startTime)
        mem=[-1]*50000
        jobs=[s for s in zip(startTime,endTime,profit)]
        jobs.sort(key=lambda x:x[0])
        startTime.sort()
        def findNextJobIndex(startTime,lastjobendtime):
            start=0
            end=len(startTime)-1
            ni=len(startTime)
            while start<=end:
                mid=(start+end)/2
                if startTime[mid]>=lastjobendtime:
                    ni=mid
                    end=mid-1
                else:
                    start=mid+1
            return ni
        def findMaxProfit(jobs,startTime,i):
            if i==n:
                return 0
            if mem[i]>-1:
                return mem[i]
            nextIndex=findNextJobIndex(startTime,jobs[i][1])
            # do and nextindex or skip to next valid job in starttime
            maxprofit=max(findMaxProfit(jobs,startTime,i+1),jobs[i][2]+findMaxProfit(jobs,startTime,nextIndex))
            mem[i]=maxprofit
            return maxprofit
        return findMaxProfit(jobs,startTime,0)

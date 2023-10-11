class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        resp = [0]*len(people)
        people = [(p,i) for i,p in enumerate(people) ]
        start=[f[0] for f in flowers]
        end=[f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)
        count=0
        for p , i in sorted(people):
            
            while start and start[0]<=p:
                heapq.heappop(start)
                count+=1
            while end and end[0] < p:
                heapq.heappop(end)
                count-=1
            resp[i]=count
        return resp


        

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals=sorted(intervals, key=lambda x:x[0])
        minheap=[0]
        for i in intervals:
            if i[0]>=minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i[1])
        return len(minheap)

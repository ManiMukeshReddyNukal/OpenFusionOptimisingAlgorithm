class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[0])
        free_rooms=[]
        heapq.heappush(free_rooms, intervals[0][1])
        for [s,d] in intervals[1:]:
            if free_rooms[0]<=s:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, d)
        return len(free_rooms)

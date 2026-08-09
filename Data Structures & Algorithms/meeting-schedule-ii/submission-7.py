"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        rooms = []
        result = 1
        intervals.sort(key=lambda x: (x.start, -x.end))
        rooms.append(intervals[0].end)
        # print([(interval.start, interval.end) for interval in intervals])
        for i in range(1, len(intervals)):
            time = intervals[i]
            start, end = time.start, time.end
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            if not rooms:
                heapq.heappush(rooms, end)
            elif start < rooms[0]:
                heapq.heappush(rooms, end)
            # print(rooms)
            result = max(result, len(rooms))
        return result


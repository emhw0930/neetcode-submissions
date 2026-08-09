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
        result = 0
        intervals.sort(key=lambda x: (x.start, -x.end))
        for i in range(len(intervals)):
            time = intervals[i]
            start, end = time.start, time.end
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            # print(rooms)
            result = max(result, len(rooms))
        return result


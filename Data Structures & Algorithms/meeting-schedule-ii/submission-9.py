"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        result = 0
        intervals.sort(key=lambda x: (x.start, -x.end))
        for time in intervals:
            start, end = time.start, time.end
            while rooms and rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            result = max(result, len(rooms))
        return result


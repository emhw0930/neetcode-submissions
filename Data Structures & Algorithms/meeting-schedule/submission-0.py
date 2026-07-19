"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorti = sorted(intervals, key=lambda x: (x.start))
        prev_end = -1
        for inter in sorti:
            x, y = inter.start, inter.end
            if x < prev_end:
                return False
            prev_end = y
        return True
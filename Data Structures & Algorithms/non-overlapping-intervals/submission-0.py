class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sort = sorted(intervals, key=lambda x: (x[1], -x[0]))
        print(sort)
        px, py = sort[0]
        count = 0
        for i in range(1, len(sort)):
            x, y = sort[i]
            if x < py:
                count += 1
                continue
            else:
                px, py = x, y
        return count
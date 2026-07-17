class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_interval = sorted(intervals, key=lambda x: (x[0], x[1]))
        print(sorted_interval)
        px, py = sorted_interval[0]
        print(sorted_interval[0])
        result = []
        for i in range(1, len(sorted_interval)):
            x = sorted_interval[i][0]
            y = sorted_interval[i][1]
            print(x, y)
            if x == px and y >= py:
                py = y
            elif x <= py and y >= py:
                py = y
            elif x <= py and y <= py:
                continue
            else:
                result.append([px, py])
                px = x
                py = y
        result.append([px, py])
        return result


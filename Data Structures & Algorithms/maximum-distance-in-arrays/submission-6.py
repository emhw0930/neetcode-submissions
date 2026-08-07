class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        fMax = [float("-inf"), 0]
        sMax = [float("-inf"), 0]
        fMin = [float("inf"), 0]
        sMin = [float("inf"), 0]

        for i in range(len(arrays)):
            maxi = arrays[i][-1]
            mini = arrays[i][0]
            if maxi > fMax[0]:
                sMax = fMax
                fMax = [maxi, i]
            elif maxi > sMax[0]:
                sMax = [maxi, i]
            if mini < fMin[0]:
                sMin = fMin
                fMin = [mini, i]
            elif mini < sMin[0]:
                sMin = [mini, i]
        
        if fMax[1] != fMin[1]:
            return abs(fMax[0] - fMin[0])
        else:
            return max(abs(fMax[0] - sMin[0]), abs(sMax[0] - fMin[0]))

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counting = [0] * 101
        expect = []
        result = 0
        for height in heights:
            counting[height] += 1
        for i, count in enumerate(counting):
            if count > 0:
                expect.extend([i] * count)
        for i in range(len(heights)):
            if expect[i] != heights[i]:
                result += 1
        return result
        
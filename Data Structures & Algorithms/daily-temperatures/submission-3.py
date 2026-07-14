class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev = stack.pop(-1)
                result[prev[1]] = i - prev[1]
            stack.append([temp, i])
        
        return result


        
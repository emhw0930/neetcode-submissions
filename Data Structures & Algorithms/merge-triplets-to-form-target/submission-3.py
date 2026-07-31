class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [False, False, False]
        for i in range(len(triplets) - 1, -1, -1):
            a, b, c = triplets[i]
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            if a == target[0]: result[0] = True
            if b == target[1]: result[1] = True
            if c == target[2]: result[2] = True
            if all(result):
                return True
        return False
            
        
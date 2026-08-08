class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0] * len(boxes)
        distance = [i for i in range(len(boxes)) if boxes[i] == '1']
        for i in range(len(boxes)):
            result[i] = sum(list(map(abs, distance)))
            distance = list(map(lambda x: x - 1, distance))
        return result
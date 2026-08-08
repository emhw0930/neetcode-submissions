class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefix = [0] * len(boxes)
        suffix = [0] * len(boxes)
        count = 0
        sumi = 0
        for i in range(len(boxes)):
            sumi += count
            prefix[i] = sumi
            if boxes[i] == '1':
                count += 1
        count = 0
        sumi = 0
        for i in range(len(boxes) - 1, -1, -1):
            sumi += count
            suffix[i] = sumi
            if boxes[i] == '1':
                count += 1
        return [p + s for p, s in zip(prefix, suffix)]

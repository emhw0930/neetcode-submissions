class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = deque()
        positive = []
        result = []
        for num in nums:
            if num < 0 :
                negative.appendleft(num ** 2)
            else:
                positive.append(num ** 2)
        print(negative)
        print(positive)
        while negative and positive:
            if negative[0] < positive[0]:
                result.append(negative.popleft())
            else:
                result.append(positive.pop(0))
        if negative:
            result.extend(negative)
        if positive:
            result.extend(positive)
        return result
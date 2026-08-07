class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        currP = 0
        currS = 0
        prefix = [0]
        sufix = [0]
        result = 0
        for i in range(k):
            currP += cardPoints[i]
            prefix.append(currP)
        for i in range(len(cardPoints) - 1, len(cardPoints) - k - 1, -1):
            currS += cardPoints[i]
            sufix.append(currS)
        for i in range(k + 1):
            result = max(prefix[i] + sufix[k - i], result)
        return result
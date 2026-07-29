class Solution:
    def reorganizeString(self, s: str) -> str:
        counting = [0] * 26
        for char in s:
            counting[ord(char) - ord('a')] += 1
        maxi = max(counting)
        if maxi > (len(s) + 1) // 2:
            return ""
        result = []

        while len(result) < len(s):
            maxIdx = counting.index(max(counting))
            result.append(chr(maxIdx + ord('a')))
            counting[maxIdx] -= 1
            if counting[maxIdx] == 0:
                continue
            temp = counting[maxIdx]
            counting[maxIdx] = float("-inf")
            secondIdx = counting.index(max(counting))
            result.append(chr(secondIdx + ord('a')))
            counting[secondIdx] -= 1
            counting[maxIdx] = temp
        return "".join(result)
        

        
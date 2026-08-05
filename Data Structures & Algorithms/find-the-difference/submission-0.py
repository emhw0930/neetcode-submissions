class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count[ord(char) - ord('a')] -= 1
        for i in range(26):
            if count[i]:
                return chr(i + ord('a'))

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1counter = Counter(s1)
        for i in range(len(s2) - n + 1):
            s2counter = Counter(s2[i:i+n])
            if s1counter == s2counter:
                return True
        return False

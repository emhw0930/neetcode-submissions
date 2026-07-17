class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l, r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count
        count = 0
        for i in range(len(s)):
            count += expand(i, i)
            if i < len(s) - 1:
                count += expand(i, i + 1)
        return count
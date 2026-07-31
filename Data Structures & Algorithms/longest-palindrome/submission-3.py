class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = False
        result = 0
        for k, v in counter.items():
            if v % 2 == 1:
                odd = True
            result += v // 2 * 2
        if odd:
            result += 1
        return result
        
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = defaultdict(int)
        maxi = 0
        curr = 0
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while len(window) > k:
                delete_key = s[l]
                window[delete_key] -= 1
                if window[delete_key] == 0:
                    del window[delete_key]
                l += 1
            curr = r - l + 1
            maxi = max(maxi, curr)

        return maxi
            
        
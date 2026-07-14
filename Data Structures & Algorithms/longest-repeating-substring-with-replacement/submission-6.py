class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        longest = 0
        left = 0
        count = {}
        maxf = 0

        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            maxf = max(maxf, count[s[i]])

            while (i - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
            longest = max(longest, i - left + 1)

        return longest
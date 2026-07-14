class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        visited = []
        left = 0

        for i in range(len(s)):
            while s[i] in visited:
                left += 1
                visited.pop(0)
            visited.append(s[i])
            maxLength = max(maxLength, i - left + 1)
        
        return maxLength
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        visited = set()
        left = 0

        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[i])
            maxLength = max(maxLength, i - left + 1)
        
        return maxLength
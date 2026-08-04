class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs)
        for i in range(len(mini)):
            for word in strs:
                if word[i] != mini[i]:
                    return mini[:i]
        return mini

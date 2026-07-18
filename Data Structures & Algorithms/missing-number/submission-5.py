class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sorted(nums)
        for i in range(len(s)):
            if i != s[i]:
                return i
        return len(s)
        
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for num in nums:
            if num:
                count += 1
            else:
                count = 0
            result = max(result, count)
        return result
        
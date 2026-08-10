class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        currSum = 0
        l = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                result = min(r - l + 1, result)
                print(r, l)
                currSum -= nums[l]
                l += 1
        if result == float('inf'):
            return 0
        return result
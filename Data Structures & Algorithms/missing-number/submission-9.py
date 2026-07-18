class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumi = len(nums)
        for i in range(len(nums)):
            sumi += i - nums[i]
        return sumi
        
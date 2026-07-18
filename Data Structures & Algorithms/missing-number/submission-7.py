class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumi = len(nums)
        for i in range(len(nums)):
            sumi += i
            sumi -= nums[i]
        return sumi
        
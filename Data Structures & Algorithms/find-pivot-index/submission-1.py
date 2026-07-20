class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums) - nums[0]

        for i in range(len(nums)):
            if l == r:
                return i
            elif i < len(nums) - 1:
                l += nums[i]
                r -= nums[i + 1]

        return -1
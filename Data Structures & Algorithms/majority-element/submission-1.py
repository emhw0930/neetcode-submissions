class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = nums[0]
        count = 0
        for ele in nums:
            if ele == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = ele
                    count = 1
        return num
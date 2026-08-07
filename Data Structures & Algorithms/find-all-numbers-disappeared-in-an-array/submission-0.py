class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seti = set(nums)
        result = []
        for i in range(len(nums)):
            if i + 1 not in seti:
                result.append(i + 1)
        return result
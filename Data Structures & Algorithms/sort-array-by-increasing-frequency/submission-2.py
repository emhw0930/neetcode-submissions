class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counting = Counter(nums)
        nums.sort(key=lambda x: (counting[x], -x))
        return nums

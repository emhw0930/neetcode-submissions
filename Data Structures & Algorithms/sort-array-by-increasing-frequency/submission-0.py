class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counting = Counter(nums)
        sorting = sorted(counting.keys(), key=lambda x: (counting[x], -x))
        print(sorting)
        result = []
        for k in sorting:
            result.extend([k] * counting[k])
        return result

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefex sum: count
        mapi = defaultdict(int)
        mapi[0] = 1
        prefex_sum = 0
        result = 0
        for num in nums:
            prefex_sum += num
            if prefex_sum - k in mapi:
                result += mapi[prefex_sum - k]
            mapi[prefex_sum] += 1
        return result

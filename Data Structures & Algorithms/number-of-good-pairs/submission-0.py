class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # dictionary {val: counts}
        # result += counts if val == nums[i] and counts > 0
        mapi = defaultdict(int)
        result = 0
        for num in nums:
            if num in mapi:
                result += mapi[num]
            mapi[num] += 1
        return result
        
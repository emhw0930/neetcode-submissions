class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # every value's count needs to be plural
        #   to satisfy 
        #       1. same value in a pair
        #       2. belong to a pair
        counter = Counter(nums)
        for value in counter.values():
            if value % 2 == 1:
                return False
        return True
        
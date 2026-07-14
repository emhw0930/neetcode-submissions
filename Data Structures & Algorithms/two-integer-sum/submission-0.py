class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictindex = {}

        for index, val in enumerate(nums):
            diff = target - val

            if diff in dictindex:
                return [dictindex[diff], index]
            
            dictindex[val] = index
        

        
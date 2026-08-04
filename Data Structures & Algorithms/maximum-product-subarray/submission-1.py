class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1
        result = max(nums)
        for num in nums:
            temp = maxi * num
            maxi = max(maxi * num, mini * num, num)
            mini = min(temp, mini * num, num)
            result = max(result, maxi)
        return result
        
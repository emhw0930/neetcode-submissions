class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = 1
        mini = 1
        result = max(nums)
        for num in nums:
            temp = maxi
            maxi = max(maxi * num, mini * num, num)
            mini = min(temp * num, mini * num, num)
            result = max(result, maxi, mini)
        return result
        
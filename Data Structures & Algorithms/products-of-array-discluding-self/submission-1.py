class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 4, 6]
        # Left product  [ 1, 1,  2, 8] # don't need the last value
        # Right product [48, 24, 6, 1]       # don't need the first value
        # expected []
        # Expected product [48, 24, 12, 8]
        n = len(nums)

        left_product = [0] * n
        right_product = [0] * n
        ans = [0] * n

        left_product[0] = 1
        right_product[n-1] = 1

        for i in range(1, n):
            left_product[i] = nums[i - 1] * left_product[i - 1] 
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i + 1] * right_product[i + 1]
        for i in range(n):
            ans[i] = left_product[i] * right_product[i]
        
        return ans
        

            
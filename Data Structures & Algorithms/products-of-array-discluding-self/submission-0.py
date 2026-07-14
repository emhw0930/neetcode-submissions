class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProd = 1
        count_zero = 0

        for num in nums:
            if num:
                totalProd = totalProd * num
            else:
                count_zero += 1
        
        if count_zero > 1:
            return [0] * len(nums)
        
        return_lst = [0] * len(nums)
        
        for i, val in enumerate(nums):
            if count_zero == 1:
                if val:
                    return_lst[i] = 0
                else:
                    return_lst[i] = totalProd
            else:
                return_lst[i] = totalProd // nums[i]
        
        return return_lst

        
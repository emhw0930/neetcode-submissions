class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8] target = 3
        # mid = 6 // 2 = 3 index = 4 val
        # 4 > 3 so right = mid - 1 = 2
        # 3 > 2 so left = mid + 1
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = ((right - left) // 2) + left
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        return -1

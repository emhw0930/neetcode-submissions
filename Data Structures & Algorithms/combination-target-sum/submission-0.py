class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        curr = []

        def dfs(index, total):
            if total == target:
                ans.append(curr.copy())
                return
            if total > target or index >= len(nums):
                return
            
            curr.append(nums[index])
            dfs(index, total+nums[index])

            curr.pop()
            dfs(index+1, total)
        
        dfs(0, 0)

        return ans

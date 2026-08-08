# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result = [root.val, abs(root.val - target)]
        def dfs(node):
            if not node:
                return
            diff = node.val - target
            if abs(diff) < result[1]:
                result[0] = node.val
                result[1] = abs(diff)
            if diff < 0:
                dfs(node.right)
            elif diff > 0:
                dfs(node.left)
            else:
                return 
        dfs(root)
        return result[0]
        
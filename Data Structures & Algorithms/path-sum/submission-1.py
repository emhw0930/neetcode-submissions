# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(node, curr, target):
            curr += node.val
            l = r = False
            if not node.left and not node.right and curr == target:
                return True
            if node.left:
                l = dfs(node.left, curr, target)
            if node.right:
                r = dfs(node.right, curr, target)
            return l or r
        return dfs(root, 0, targetSum) 
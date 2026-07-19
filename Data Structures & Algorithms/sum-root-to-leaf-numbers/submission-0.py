# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sumi = 0

        def dfs(node, value):
            value *= 10
            value += node.val
            if not node.left and not node.right:
                nonlocal sumi
                sumi += value
                return
            if node.left:
                dfs(node.left, value)
            if node.right:
                dfs(node.right, value)
            
        dfs(root, 0)

        return sumi
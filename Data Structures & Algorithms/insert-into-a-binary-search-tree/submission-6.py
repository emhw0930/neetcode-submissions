# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, target):
            if not node:
                return TreeNode(val)
            if target < node.val:
                self.place = node
                node.left = dfs(node.left, target)
            elif target > node.val:
                self.place = node
                node.right = dfs(node.right, target)
            return node
        return dfs(root, val)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.result = None
        def dfs(node):
            if not node:
                return 
            if node == p or node == q:
                self.result = node
                return
            if node.val > max(p.val, q.val):
                dfs(node.left)
            elif node.val < min(p.val, q.val):
                dfs(node.right)
            else:
                self.result = node
                return
        dfs(root)
        return self.result
        
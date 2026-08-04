# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.result = None
        def dfs(node):
            if not node:
                return [False, False]
            l = dfs(node.left)
            r = dfs(node.right)
            curr = [l[0] or r[0] or node == p, l[1] or r[1] or node == q]
            if curr[0] and curr[1] and not self.result:
                self.result = node
            return curr
        dfs(root)
        return self.result
        
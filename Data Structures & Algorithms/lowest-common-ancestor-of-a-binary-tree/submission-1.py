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
            left = dfs(node.left)
            right = dfs(node.right)
            curr = [node == p, node == q]
            # print(node.val)
            # print("curr: ", curr)
            # print("left: ", left)
            # print("right: ", right)
            if (left[0] or right[0] or curr[0]) and (left[1] or right[1] or curr[1]):
                self.result = node
                # print('if case: ', self.result)
                return [False, False]
            return [left[0] or right[0] or curr[0], left[1] or right[1] or curr[1]]
        dfs(root)
        return self.result            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            if not nodeq or not nodep or nodep.val != nodeq.val:
                return False
            left = dfs(nodep.left, nodeq.left)
            right = dfs(nodep.right, nodeq.right)
            return left and right

        return dfs(p, q)
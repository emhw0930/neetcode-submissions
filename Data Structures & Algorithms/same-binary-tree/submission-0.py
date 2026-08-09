# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(nodep, nodeq):
            left, right = True, True
            if not nodep and not nodeq:
                return True
            if nodep and not nodeq or nodeq and not nodep:
                return False
            if nodep.val != nodeq.val:
                return False
            else:
                left = dfs(nodep.left, nodeq.left)
                right = dfs(nodep.right, nodeq.right)
            return left and right

        return dfs(p, q)
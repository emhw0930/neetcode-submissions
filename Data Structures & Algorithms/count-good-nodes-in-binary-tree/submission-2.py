# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxnum):
            if not node:
                return 0
            result = 0
            if node.val >= maxnum:
                result += 1
            maxnum = max(maxnum, node.val)
            result += dfs(node.left, maxnum)
            result += dfs(node.right, maxnum)
            return result
        return dfs(root, root.val)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node, maxnum):
            if not node:
                return
            if node.val >= maxnum:
                self.result += 1
                maxnum = max(maxnum, node.val)
            dfs(node.left, maxnum)
            dfs(node.right, maxnum)
        dfs(root, root.val)
        return self.result

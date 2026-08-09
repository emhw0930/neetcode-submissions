# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 1
        self.result = None
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val, self.count)
            if self.count > k:
                return
            if self.count == k:
                self.result = node.val
                self.count += 1
                return
            else:
                self.count += 1
            dfs(node.right)
        dfs(root)
        return self.result
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.in_order = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.in_order.append(node)
            dfs(node.right)
        dfs(root)
        node1, node2 = None, None
        for i in range(len(self.in_order) - 1):
            if self.in_order[i].val > self.in_order[i + 1].val:
                node2 = self.in_order[i + 1]
                if not node1:
                    node1 = self.in_order[i]
                else:
                    break
        node1.val, node2.val = node2.val, node1.val

        
        
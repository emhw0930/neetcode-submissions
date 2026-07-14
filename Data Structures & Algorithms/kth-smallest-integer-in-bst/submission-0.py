# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def inOrderTrav(root, k):
            if not root:
                return
            inOrderTrav(root.left, k)
            lst.append(root.val)
            inOrderTrav(root.right, k)
        inOrderTrav(root, k)
        return lst[k-1]
        
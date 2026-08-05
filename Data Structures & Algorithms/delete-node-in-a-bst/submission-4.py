class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:                          # found it
            if not root.left:
                return root.right      # 0 or 1 child
            if not root.right:
                return root.left
            succ = root.right          # 2 children: in-order successor
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return None
            if key < node.val:
                node.left = dfs(node.left, key)
            elif key > node.val:
                node.right = dfs(node.right, key)
            else: # found the key
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else: # two children
                    nexdel = node.right
                    while nexdel.left:
                        nexdel = nexdel.left
                    node.val = nexdel.val
                    node.right = dfs(node.right, node.val)
            return node
        return dfs(root, key)
                    

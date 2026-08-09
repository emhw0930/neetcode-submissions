# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            layer = []
            for _ in range(len(queue)):
                nex = queue.popleft()
                if nex.left:
                    queue.append(nex.left)
                if nex.right:
                    queue.append(nex.right)
                layer.append(nex.val)
            result.append(layer[-1])
        return result        
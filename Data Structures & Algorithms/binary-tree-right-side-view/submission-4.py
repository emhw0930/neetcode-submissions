# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        if root:
            queue.append(root)
        res_lst = []
        while queue:
            cuur_lst = []
            for _ in range(len(queue)):
                node = queue.popleft()
                cuur_lst.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res_lst.append(cuur_lst[-1])
        return res_lst 





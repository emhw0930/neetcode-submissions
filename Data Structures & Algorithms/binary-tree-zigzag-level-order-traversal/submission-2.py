# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        def bfs(node):
            queue = deque([node])
            level = 1
            result = []
            while queue:
                lst = deque()
                for _ in range(len(queue)):
                    nex = queue.popleft()
                    if level % 2 == 0:
                        lst.appendleft(nex.val)
                    else:
                        lst.append(nex.val)
                    if nex.left:
                        queue.append(nex.left)
                    if nex.right:
                        queue.append(nex.right)
                level += 1
                result.append(lst)
            return result
        
        order = bfs(root)
        
        return order


        
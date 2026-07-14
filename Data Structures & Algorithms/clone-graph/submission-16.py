"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}
        old_to_new[node] = Node(node.val)
        queue = deque()
        queue.append(node)
        
        while queue:
            nex = queue.popleft()
            for neighbor in nex.neighbors:
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                old_to_new[nex].neighbors.append(old_to_new[neighbor])
                
        
        return old_to_new[node] if old_to_new[node] else None

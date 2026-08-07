# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        def nextnode(node, n):
            # the first node needs to be deleted as well
            count = 0
            while node and count <= n:
                node = node.next
                count += 1
            return node
        curr = head
        count = 0
        while curr:
            if count == m - 1:
                curr.next = nextnode(curr, n)
                count = 0
            else:
                count += 1
            curr = curr.next
        return head
        
        
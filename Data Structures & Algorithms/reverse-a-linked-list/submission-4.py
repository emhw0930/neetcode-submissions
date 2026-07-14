# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0 -> 1 -> 2 -> 3 -> None
        # None <- 0 <- 1 <- 2 <- 3
        res = None
        curr = head
        while curr:
            rest = curr.next
            curr.next = res
            res = curr
            curr = rest
        return res
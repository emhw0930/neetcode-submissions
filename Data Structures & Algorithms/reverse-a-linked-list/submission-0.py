# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        rest = None
        while curr:
            save_rest = curr.next # save 1, 2, 3
            curr.next = rest # 0 -> None
            rest = curr # rest = 0 -> None
            curr = save_rest

        return rest
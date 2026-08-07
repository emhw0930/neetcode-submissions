# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # zero index 
        dummy = ListNode(0, head)
        dcurr = dummy
        left, right = left - 1, right - 1
        ptr = 0
        curr = head
        while ptr < left:
            dcurr = dcurr.next
            curr = curr.next
            ptr += 1
        rest = None
        ptr = 0
        while curr and ptr <= (right - left):
            ptr += 1
            temp = curr.next
            curr.next = rest
            rest = curr
            curr = temp
        dcurr.next = rest
        while dcurr.next:
            dcurr = dcurr.next
        dcurr.next = curr
        return dummy.next        
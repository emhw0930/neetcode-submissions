# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [0] -> [1] -> [2] -> [3] -> None
        # [0] -> None | [1] -> [2] -> [3] -> None
        # [1] -> [0] -> None | [2] -> [3] -> None
        # [2] -> [1] -> [0] -> None | [3] -> None
        # [3] -> [2] -> [1] -> [0] -> None | None

        # curr = [0] -> [1] -> [2] -> [3] -> None
        # prev = None
        # curr = [1] -> [2] -> [3] -> None
        # prev = [0] -> None
        # curr = [2] -> [3] -> None
        # prev = [1] -> [0] -> None
        # curr = [3] -> None
        # prev = [2] -> [1] -> [0] -> None
        # curr = None
        # prev = [3] -> [2] -> [1] -> [0] -> None

        curr = head
        prev = None

        while curr:
            saved = curr.next
            curr.next = prev
            prev = curr
            curr = saved

        return prev






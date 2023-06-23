# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev = None
        present = head
        future = present.next

        while present:
            present.next = prev
            prev = present
            present = future

            if future:
                future = future.next

        return prev
                
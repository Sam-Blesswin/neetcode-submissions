# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        left = head
        right = prev

        while left and right and left.next != right:
            lNext = left.next
            left.next = right

            rNext = right.next
            right.next = lNext

            left = lNext
            right = rNext
        
        
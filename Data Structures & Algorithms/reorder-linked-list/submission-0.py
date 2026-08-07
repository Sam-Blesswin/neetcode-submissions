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
        right = slow
        while right:
            next = right.next
            right.next = prev
            prev = right
            right = next

        right = prev
        left = head

        while left and right and left.next != right:
            lNext = left.next
            left.next = right
            left = lNext

            rNext = right.next
            right.next = left
            right = rNext





        

        
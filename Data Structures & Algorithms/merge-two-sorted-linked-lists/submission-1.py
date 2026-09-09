# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        while list1 and list2:
            if list1.val <= list2.val:
                if not head:
                    head.next = list1
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                if not head:
                    head.next = list2
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return head.next




        
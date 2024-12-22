"""
203. Remove Linked List Elements
Easy
Topics
Companies
Given the head of a linked list and an integer val,
 remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = None
        current = head
        if not head:
            return head
        while current and current.next:
            next = current.next
            if current.val == val:
                if prev is None:
                    head = head.next




            prev = current
            current = next
        return head


headA = ListNode(4)
headA.next = ListNode(0)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)
headA.next.next.next.next.next = ListNode(1)
headA.next.next.next.next.next.next = ListNode(5)
print(Solution().removeElements(headA, 1))

"""
160. Intersection of Two Linked Lists
Easy
Topics
Companies
Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA


headA = ListNode(4)
headA.next = ListNode(0)
headA.next.next = ListNode(3)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)
headA.next.next.next.next.next = ListNode(1)
headA.next.next.next.next.next.next = ListNode(5)

headB = ListNode(1)
headB.next = ListNode(4)
headB.next.next = ListNode(2)
headB.next.next.next = ListNode(4)
headB.next.next.next.next = ListNode(1)
headB.next.next.next.next.next = ListNode(5)

print(Solution().getIntersectionNode(headA, headB))

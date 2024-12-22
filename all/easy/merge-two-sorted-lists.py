# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

            if list1:
                tail.next = list1
            if list2:
                tail.next = list2
        return dummy.next


l13 = ListNode(4, None)
l12 = ListNode(3, l13)
l11 = ListNode(1, l12)


l23 = ListNode(4, None)
l22 = ListNode(2, l23)
l21 = ListNode(1, l22)

result = Solution().mergeTwoLists(l11, l21)
print(result)



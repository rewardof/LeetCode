"""
234. Palindrome Linked List
Easy Topics Companies
Given the head of a singly linked list, return true if it is a
palindrome or false otherwise.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        as_list = []
        current = head
        while current:
            as_list.append(current.val)
            current = current.next
        i, j = 0, len(as_list) - 1
        while i < j:
            if as_list[i] != as_list[j]:
                return False
            i += 1
            j -= 1
        return True


def isPalindrome(head: ListNode) -> bool:
    if not head or not head.next:
        return True  # A single node or empty list is always a palindrome

    # Step 1: Find the middle of the list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half of the list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Step 3: Compare the two halves
    first, second = head, prev
    while second:  # second half is shorter or equal
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


headA = ListNode(4)
headA.next = ListNode(0)
headA.next.next = ListNode(1)
headA.next.next.next = ListNode(2)
headA.next.next.next.next = ListNode(4)
headA.next.next.next.next.next = ListNode(1)
headA.next.next.next.next.next.next = ListNode(5)
print(Solution().isPalindrome(headA))

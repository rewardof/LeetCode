"""
705. Design HashSet
Easy
Topics
Companies
Design a HashSet without using any built-in hash table libraries.
"""


class ListNode:
    """A node in the linked list."""

    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet:
    def __init__(self):
        self.BASE = 769  # A prime number for better hashing
        self.data = [None] * self.BASE  # Array of linked list heads

    def _hash(self, key):
        """Hash function to compute index."""
        return key % self.BASE

    def add(self, key: int) -> None:
        """Add a key to the HashSet."""
        index = self._hash(key)
        if not self.data[index]:  # No collision, initialize linked list
            self.data[index] = ListNode(key)
            return

        # Traverse the linked list to check if the key already exists
        current = self.data[index]
        while current:
            if current.key == key:  # Key already exists, do nothing
                return
            if not current.next:  # Reached the end, insert the key
                current.next = ListNode(key)
                return
            current = current.next

    def remove(self, key: int) -> None:
        """Remove a key from the HashSet."""
        index = self._hash(key)
        current = self.data[index]
        if not current:  # Bucket is empty
            return

        # If the key is at the head of the list
        if current.key == key:
            self.data[index] = current.next
            return

        # Traverse the linked list to find and remove the key
        prev = current
        while current:
            if current.key == key:
                prev.next = current.next  # Remove the node
                return
            prev, current = current, current.next

    def contains(self, key: int) -> bool:
        """Check if the key exists in the HashSet."""
        index = self._hash(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return True
            current = current.next
        return False



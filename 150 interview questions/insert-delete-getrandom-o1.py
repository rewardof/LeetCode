"""
380. Insert Delete GetRandom O(1)
"""
import random

import random


class RandomizedSet:

    def __init__(self):
        self.hash_table = {}  # Stores {val: index} mappings
        self.array = []  # Stores values for O(1) random access

    def insert(self, val: int) -> bool:
        if val in self.hash_table:
            return False
        self.hash_table[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_table:
            return False

        index = self.hash_table[val]  # Get index of `val`
        last_element = self.array[-1]  # Last element in array

        if index != len(self.array) - 1:  # Swap only if it's not the last element
            self.array[index] = last_element
            self.hash_table[last_element] = index

        self.array.pop()  # Remove last element
        del self.hash_table[val]  # Remove from hash table
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)  # O(1) random selection


class RandomizedSet2:

    def __init__(self):
        self.hash_table = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hash_table:
            return False
        self.array.append(val)
        self.hash_table[val] = len(self.array) - 1

    def remove(self, val: int) -> bool:
        if val not in self.hash_table:
            return False

        index = self.hash_table[val]
        last_element = self.array[-1]

        self.array[index] = last_element
        self.hash_table[last_element] = index

        self.array.pop()
        del self.hash_table[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)


# ✅ Test Cases
obj = RandomizedSet()
print(obj.insert(1))  # True
print(obj.insert(2))  # True
print(obj.remove(1))  # True
print(obj.insert(3))  # True
print(obj.remove(2))  # True
print(obj.getRandom())  # Should return 3 (only element left)


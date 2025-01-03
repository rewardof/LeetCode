"""
744. Find Smallest Letter Greater Than Target
"""
from typing import List


class Solution2:
    """
    this solution is linear search solution
    """

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        closest = float('inf')
        for char in letters:
            if ord(target) < ord(char) < closest:
                closest = ord(char)

        return chr(closest) if closest != float('inf') else letters[0]


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                high = mid - 1
            elif letters[mid] < target:
                low = mid + 1
            else:
                return letters[mid + 1] if mid + 1 < len(letters) else letters[0]
        return letters[low] if low < len(letters) else letters[0]


letters = ["e", "e", "g", "g"]
target = "g"
print(Solution().nextGreatestLetter(letters, target))

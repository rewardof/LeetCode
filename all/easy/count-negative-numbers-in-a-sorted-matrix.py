"""
1351. Count Negative Numbers in a Sorted Matrix
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        number_negatives = 0
        for arr in grid:
            index = find_first_negative(arr)
            if index == -1:
                continue
            else:
                number_negatives += len(arr) - index
        return number_negatives


def find_first_negative(arr: list[int]) -> int:
    low, high = 0, len(arr) - 1
    first_negative_index = -1  # Default: No negative elements found

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < 0:  # Found a negative element
            first_negative_index = mid  # Update index
            high = mid - 1  # Search left for earlier negative elements
        else:  # Positive or zero
            low = mid + 1  # Search right

    return first_negative_index


arr = [4, 3, 2, 1, -2, -1]
print(find_first_negative(arr))

"""
1608. Special Array With X Elements Greater Than or Equal X
"""
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        for i in range(len(nums) + 1):
            index = find_last_less_than(nums, i)
            count = l - index - 1
            if count == i:
                return i
        return -1


def find_last_less_than(sorted_arr: List[int], target: int) -> int:
    low, high = 0, len(sorted_arr) - 1
    result = -1  # To store the index of the last less-than element

    while low <= high:
        mid = (low + high) // 2

        if sorted_arr[mid] < target:
            result = mid  # Update the result to the current index
            low = mid + 1  # Move to the right half to find the last such element
        else:
            high = mid - 1  # Move to the left half

    return result


nums = [3, 5]
k = 6
print(Solution().specialArray(nums))

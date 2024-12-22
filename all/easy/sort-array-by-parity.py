"""
905. Sort Array By Parity
Easy
Topics
Companies
Given an integer array nums, move all the even integers
at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
from typing import List


class Solution2:
    """my solution"""

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_index = 0
        change = True
        for i, value in enumerate(nums):
            if value % 2 != 0:
                if change:
                    last_index = i
                    change = False
            else:
                nums[last_index], nums[i] = nums[i], nums[last_index]
                last_index += 1
        return nums


class Solution:
    """optimized solution"""

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        last_index = 0
        for i, value in enumerate(nums):
            if value % 2 == 0:
                if i != last_index:
                    nums[last_index], nums[i] = nums[i], nums[last_index]
                last_index += 1
        return nums


nums = [1, 0, 3, 2]

print(Solution().sortArrayByParity(nums))

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
 You may assume that the majority element always exists in the array.
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = dict()
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key, value in nums_dict.items():
            if value > len(nums) // 2:
                return key


nums = [2, 2, 1, 1, 1, 2, 2]
print(Solution().majorityElement(nums))
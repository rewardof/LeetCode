"""
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
"""
from typing import List


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 2:
                return nums[i] - 1
        return nums[-1] + 1 if len(nums) - nums[-1] == 1 else 0


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summa = sum(nums)
        return (len(nums) * len(nums) + 1) - summa

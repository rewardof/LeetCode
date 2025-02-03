"""
561. Array Partition
"""
from typing import List


class Solution:
    """
    Easy solution
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[0:len(nums):1])


class Solution2:
    """
    Easy solution
    """
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[0:len(nums):1])


print(4.0.is_integer())
"""
645. Set Mismatch
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l, unique_sum = len(nums), sum(set(nums))
        return [l * (l + 1) // 2 - unique_sum, sum(nums) - unique_sum]

# Before
class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        unique_sum = sum(set(nums))
        expected_sum = l * (l + 1) // 2
        real_sum = sum(nums)
        dublicate = real_sum - unique_sum
        missing = expected_sum - unique_sum
        return [dublicate, missing]


# After
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [len(nums) * (len(nums) + 1) // 2 - sum(set(nums)), sum(nums) - sum(set(nums))]
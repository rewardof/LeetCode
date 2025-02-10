"""
3010. Divide an Array Into Subarrays With Minimum Cost I
"""
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        first = nums[0]
        nums.sort()
        if first == nums[0] or first == nums[1]:
            first = nums[2]
        return first + nums[0] + nums[1]



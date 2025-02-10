"""
1913. Maximum Product Difference Between Two Pairs
"""
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return nums[0] * nums[1] - nums[-1] * nums[-2]


nums = [5, 6, 2, 7, 4]
print(Solution().maxProductDifference(nums))

"""
1464. Maximum Product of Two Elements in an Array
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2] - 1) * (nums[-1] - 1)


nums = [3, 4, 5, 2]
print(Solution().maxProduct(nums))
# (nums[i] - 1) * (nums[j] - 1).

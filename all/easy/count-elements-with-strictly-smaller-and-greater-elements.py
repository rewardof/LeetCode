"""
2148. Count Elements With Strictly Smaller and Greater Elements
"""
from collections import Counter
from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        counts = Counter(nums)
        return max(len(nums) - counts[nums[0]] - counts[nums[-1]], 0)

    def countElements2(self, nums: List[int]) -> int:
        min_value, max_value = min(nums), max(nums)
        counts = Counter(nums)
        return max(len(nums) - counts[min_value] - counts[max_value], 0)


nums = [-71, -71, 93, -71, 40]
print(Solution().countElements2(nums))

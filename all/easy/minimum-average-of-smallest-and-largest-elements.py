"""
3194. Minimum Average of Smallest and Largest Elements
"""
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        min_average = 1000
        l = len(nums)
        for i in range(l // 2):
            min_average = min(min_average, (nums[i] + nums[l - i - 1]) / 2)
        return min_average


nums1 = [1, 9, 8, 3, 10, 5]
print(Solution().minimumAverage(nums1))

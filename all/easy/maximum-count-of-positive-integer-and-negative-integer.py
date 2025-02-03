"""
2529. Maximum Count of Positive Integer and Negative Integer
"""
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Find the index of the first positive number
        low, high = 0, len(nums) - 1
        first_positive = len(nums)  # Default to no positive numbers
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > 0:
                first_positive = mid
                high = mid - 1
            else:
                low = mid + 1

        # Find the index of the last negative number
        low, high = 0, len(nums) - 1
        last_negative = -1  # Default to no negative numbers
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < 0:
                last_negative = mid
                low = mid + 1
            else:
                high = mid - 1

        # Count positive and negative numbers
        positive_count = len(nums) - first_positive
        negative_count = last_negative + 1

        # Return the maximum count
        return max(positive_count, negative_count)


nums = [-3, -2, -1, 0, 0, 1, 2]
print(Solution().maximumCount(nums))

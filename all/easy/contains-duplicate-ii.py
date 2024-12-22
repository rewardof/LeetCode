"""
Given an integer array nums and an integer k, return true
if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for i in range(len(nums)):
            if nums[i] in nums_dict and i - nums_dict[nums[i]] <= k:
                return True
            else:
                nums_dict[nums[i]] = i
        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
# print(Solution().containsNearbyDuplicate(nums, k))



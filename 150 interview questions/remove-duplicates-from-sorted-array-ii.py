"""
80. Remove Duplicates from Sorted Array II
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count_duplicates = 1
        last_index = 1
        for index in range(1, len(nums)):
            if nums[index] == nums[index - 1]:
                count_duplicates += 1
            else:
                count_duplicates = 1

            if count_duplicates <= 2:
                nums[last_index] = nums[index]
                last_index += 1
        print(nums)
        return last_index


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(Solution().removeDuplicates(nums))

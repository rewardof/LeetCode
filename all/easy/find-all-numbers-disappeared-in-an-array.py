"""
Given an array nums of n integers where nums[i] is in the range [1, n],
 return an array of all the integers in the range [1, n] that do not appear in nums.
"""
from collections import Counter
from typing import List


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for num in nums:
            nums_dict[num] = 0

        num = 1
        result = []
        while num <= len(nums):
            if num not in nums_dict:
                result.append(num)
            num += 1
        return result


class Solution3:
    """
    AI solution
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        return [num for num in range(1, len(nums) + 1) if num not in nums_set]


class Solution4:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Step 1: Mark the indices based on the values
        for num in nums:
            index = abs(num) - 1  # Convert value to index
            nums[index] = -abs(nums[index])  # Mark as visited by making it negative

        print(nums)
        # Step 2: Find indices that were not marked
        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]

        return result


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for num in nums:
            count[num - 1] += 1
        return [i + 1 for i in range(len(nums)) if count[i] == 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Counter(nums))
print(Solution().findDisappearedNumbers(nums))

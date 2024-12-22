"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such
 that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
 where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            diff = target - numbers[i] - numbers[j]

            if diff == 0:
                break
            elif diff > 0:
                i += 1
            else:
                j -= 1

        return [i + 1, j + 1]


numbers = [2, 3, 4]
target = 6
print(Solution().twoSum(numbers, target))

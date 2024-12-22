"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:  # End of a range
                result.append(
                    f"{nums[start]}->{nums[i - 1]}" if start != i - 1 else str(nums[start])
                )
                start = i  # Start a new range

        # Add the last range
        result.append(
            f"{nums[start]}->{nums[-1]}" if start != len(nums) - 1 else str(nums[start])
        )

        return result


nums = [0, 2, 3, 4, 6, 8, 9]
print(Solution().summaryRanges(nums))

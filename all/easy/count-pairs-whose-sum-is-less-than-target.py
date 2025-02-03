"""
2824. Count Pairs Whose Sum is Less than Target
"""
import bisect
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i, num in enumerate(nums):
            pair = target - num
            index = bisect.bisect_left(nums, pair, i + 1)
            count += index - (i + 1)
        return count


nums = [-1, 1, 2, 3, 1]
target = 2
print(Solution().countPairs(nums, target))

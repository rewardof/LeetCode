"""
1051. Height Checker
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i, j in zip(expected, heights):
            if i != j:
                count += 1
        return count


heights = [1, 1, 4, 2, 1, 3]
print(Solution().heightChecker(heights))

"""
11. Container With Most Water
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > max_area:
                max_area = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area




height = [1, 1]
print(Solution().maxArea(height))

"""
1. iterate ove
2. har bir stepda eski max height bilan taqqoslash kerak

"""
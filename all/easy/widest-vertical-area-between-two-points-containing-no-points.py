"""
1637. Widest Vertical Area Between Two Points Containing No Points
"""
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = 0
        initial = points[0]
        for i in points:
            max_width = max(max_width, i[0] - initial[0])
            initial = i
        return max_width

    def maxWidthOfVerticalArea2(self, points: List[List[int]]) -> int:
        x = [i[0] for i in points]
        x.sort()
        prev = x[0]
        max_width = 0
        for i in x:
            max_width = max(max_width, i - prev)
            prev = i
        return max_width


points = [[8, 7], [9, 9], [7, 4], [9, 7]]
print(Solution().maxWidthOfVerticalArea(points))

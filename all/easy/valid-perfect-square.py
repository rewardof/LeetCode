"""
367. Valid Perfect Square
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        while low <= high:
            mid = (low + high) // 2
            double = mid * mid
            if double > num:
                high = mid - 1
            elif double < num:
                low = mid + 1
            else:
                return True
        return False

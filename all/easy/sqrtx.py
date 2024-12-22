"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            guess = mid * mid
            if guess == x:
                return mid
            elif guess < x:
                low = mid + 1
            else:
                high = mid - 1
        return high


class Solution2:
    """
    AI solution
    """
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            guess = mid * mid
            if guess == x:
                return mid
            elif guess < x:
                low = mid + 1
            else:
                high = mid - 1
        return high

x = 65
result = Solution().mySqrt(x)
print(result)

"""
231. Power of Two
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        return is_power_of_two(n)


def is_power_of_two(n: int | float):
    n = n / 2
    if not n.is_integer():
        return False
    if int(n) == 1:
        return True
    else:
        return is_power_of_two(n)


n = 17
print(Solution().isPowerOfTwo(n))

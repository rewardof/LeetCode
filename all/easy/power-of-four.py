"""
342. Power of Four
"""
from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 4 == 0:
            n = n // 4
        else:
            return False
        if n == 1:
            return True
        else:
            return self.isPowerOfFour(n)


class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log(n, 4) == int(log(n, 4))


n = 16
print(Solution2().isPowerOfFour(n))

"""
326. Power of Three
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        if n % 3 == 0:
            n = n // 3
        else:
            return False
        if n == 1:
            return True
        else:
            return self.isPowerOfThree(n)


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0


n = 243
print(Solution2().isPowerOfThree(n))

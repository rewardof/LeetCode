"""
441. Arranging Coins
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (low + high) // 2
            summa = mid * (mid + 1) // 2
            if summa == n:
                return mid
            elif summa < n:
                low = mid + 1
            else:
                high = mid - 1
        return high


n = 2
print(Solution().arrangeCoins(n))

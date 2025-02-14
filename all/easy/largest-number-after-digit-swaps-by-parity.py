"""
2231. Largest Number After Digit Swaps by Parity
"""

import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        odds = sorted([i for i in digits if i % 2 != 0], reverse=True)
        evens = sorted([i for i in digits if i % 2 == 0], reverse=True)
        merged = [str(odds.pop(0)) if i % 2 != 0 else str(evens.pop(0)) for i in digits]
        return int(''.join(merged))


class Solution2:
    """
    interesting solution from leetcode
    """
    def largestInteger(self, num: int) -> int:
        odd_heap = []
        even_heap = []

        num = str(num)
        for char in num:
            if int(char) % 2 == 0:
                heapq.heappush(even_heap, -int(char))
            else:
                heapq.heappush(odd_heap, -int(char))

        res = []
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                digit = - heapq.heappop(even_heap)
            else:
                digit = - heapq.heappop(odd_heap)
            res.append(str(digit))

        return int("".join(res))


num = 65875
print(Solution2().largestInteger(num))

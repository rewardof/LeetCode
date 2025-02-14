"""
2164. Sort Even and Odd Indices Independently
"""
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        """first solution"""
        odds = []
        evens = []
        ans = []
        for index, num in enumerate(nums):
            if index % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        evens.sort(reverse=True)
        odds.sort(reverse=False)
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(evens.pop())
            else:
                ans.append(odds.pop())
        return ans

    def sortEvenOdd2(self, nums: List[int]) -> List[int]:
        """
        optimized solution
        """
        odds = []
        evens = []
        ans = []
        for index, num in enumerate(nums):
            if index % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        evens.sort(reverse=True)
        odds.sort(reverse=False)
        h, j = len(evens), len(odds)
        for i in range(len(nums)):
            if i % 2 == 0:
                ans.append(evens[h - 1])
                h -= 1
            else:
                ans.append(odds[j - 1])
                j -= 1
        return ans

    def sortEvenOdd3(self, nums: List[int]) -> List[int]:
        evens = sorted(nums[0::2])
        odds = sorted(nums[1::2], reverse=True)

        ans = [0] * len(nums)

        ans[0::2] = evens
        ans[1::2] = odds
        return ans


nums = [1, 2, 3, 4, 5, 6, 7]
print(Solution().sortEvenOdd3(nums))

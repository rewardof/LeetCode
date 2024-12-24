"""
594. Longest Harmonious Subsequence
"""
from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        counter = Counter(nums_sorted)
        min_value = nums_sorted[0]
        max_value = nums_sorted[0]
        max_length = 0
        for num in nums_sorted:
            if num != min_value:
                if max_value == num:
                    continue
                max_value, min_value = num, max_value
                if max_value - min_value == 1:
                    length = counter[min_value] + counter[max_value]
                    max_length = length if length > max_length else max_length
        return max_length

    def findLHS2(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_length = 0
        for key, value in counter.items():
            pair = key + 1
            if pair in counter:
                length = value + counter[pair]
                max_length = length if length > max_length else max_length
        return max_length


nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(Solution().findLHS(nums))
